#!/bin/bash -l
#SBATCH --account=pawsey0110-gpu
#SBATCH --job-name=mdrun_hIAPP_GLC_1M
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --export=ALL


set -euo pipefail

cd "$SLURM_SUBMIT_DIR"

module use /software/projects/pawsey0110/setonix/modules/zen3/gcc/12.1.0
module load gromacs/2026.2-gpu+plumed

export FI_CXI_DEFAULT_VNI=$(od -vAn -N4 -tu < /dev/urandom)
export GMX_LOG_BUFFER=0

module list
which gmx_mpi
gmx_mpi --version

# Starting .gro structure for energy minimisation; change this filename when using the script for a different system.
START_GRO=${START_GRO:-hIAPP_GLC_1M_final.gro}

# grompp prepares/checks each stage and writes the .tpr input file.
# Run it as a single CPU task with GPU-aware MPI disabled to avoid the Setonix grompp crash seen in the GPU runtime path.
grompp_cpu() {
  env MPICH_GPU_SUPPORT_ENABLED=0 OMP_NUM_THREADS=1 GMX_OPENMP_MAX_THREADS=1 srun -N 1 -n 1 -c 1 --cpu-bind=cores gmx_mpi grompp "$@"
}

# Energy minimisation mdrun is kept CPU-only; the 3-GPU launch is reserved for the NVT/NPT dynamics stages.
mdrun_cpu() {
  env MPICH_GPU_SUPPORT_ENABLED=0 OMP_NUM_THREADS=1 GMX_OPENMP_MAX_THREADS=1 srun -N 1 -n 1 -c 1 --cpu-bind=cores gmx_mpi mdrun "$@"
}

# mdrun runs the actual dynamics. This GPU launch uses 1 MPI task, 8 CPU cores per task, and 1 GPU per task.
# GMX_FORCE_GPU_AWARE_MPI=1 tells GROMACS to use GPU-aware MPI for the GPU mdrun step.
mdrun_gpu() {
  env MPICH_GPU_SUPPORT_ENABLED=1 GMX_FORCE_GPU_AWARE_MPI=1 OMP_NUM_THREADS=8 GMX_OPENMP_MAX_THREADS=8 srun -N 1 -n 1 -c 8 --gres=gpu:1 --gpus-per-task=1 --gpu-bind=closest gmx_mpi mdrun "$@"
}

test -f "$START_GRO"
test -f topol.top
# index.ndx is used by grompp; for these MDP files it must contain System, Protein, and non-Protein groups.
test -f index.ndx
test -f 01_energy_min.mdp
test -f 02_nvt_150K_posres.mdp
test -f 03_nvt_310K_posres.mdp
test -f 04_npt_310K_posres.mdp

echo "Starting 04_npt_310_posres"
grompp_cpu -f 04_npt_310K_posres.mdp -c 03_nvt_310_posres/03_nvt_310_posres.gro -r 01_em/01_em.gro -t 03_nvt_310_posres/03_nvt_310_posres.cpt -p topol.top -n index.ndx -o 04_npt_310_posres/04_npt_310_posres.tpr -po 04_npt_310_posres/04_npt_310_posres_mdout.mdp -pp 04_npt_310_posres/04_npt_310_posres_processed.top -maxwarn 1

mdrun_gpu -deffnm 04_npt_310_posres/04_npt_310_posres -nb gpu -pme gpu -ntomp 8 -pin on -v

echo "All equilibration stages finished successfully."
