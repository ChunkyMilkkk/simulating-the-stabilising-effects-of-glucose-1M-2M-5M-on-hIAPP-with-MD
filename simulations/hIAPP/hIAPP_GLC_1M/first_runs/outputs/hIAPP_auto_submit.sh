#!/bin/bash --login
#SBATCH --partition=work
#SBATCH --job-name="GLC_1M_hIAPP"
#SBATCH --time=24:00:00
#SBATCH --account=pawsey0110
#SBATCH --ntasks=120
#SBATCH --ntasks-per-node=120
#SBATCH --cpus-per-task=1
#SBATCH --mem=200G
#SBATCH --export=ALL
#=============================================================

#======START=====
module load slurm
echo "The current job ID is $SLURM_JOB_ID"
echo "Running on $SLURM_JOB_NUM_NODES nodes"
echo "Using $SLURM_NTASKS_PER_NODE tasks per node"
echo "A total of $SLURM_NTASKS tasks is used"
echo "Node list:"
sacct --format=JobID,NodeList%100 -j $SLURM_JOB_ID

# Load modules
# Modules and etc

module use /software/projects/pawsey0110/setonix/modules/zen3/gcc/12.1.0/
module load gromacs/5.0.7-feg54bf

export OMP_NUM_THREADS=1

# Pawsey want us to to use this when using less than a full node
# Temporal workaround for avoiding Slingshot issues on shared nodes:
export FI_CXI_DEFAULT_VNI=$(od -vAn -N4 -tu < /dev/urandom)

# Before submitting this script, run the following commands:

# grompp -f  md_npt_run1.mdp -c 04_npt_310_posres.gro -p  topol.top  -n index.ndx  -o GLC_1M_hIAPP.tpr  ;

# cp GLC_1M_hIAPP.tpr GLC_1M_hIAPP0.tpr ;
# cp GLC_1M_hIAPP.tpr GLC_1M_hIAPP1.tpr ;
# cp GLC_1M_hIAPP.tpr GLC_1M_hIAPP2.tpr ;

# editconf -f 04_npt_310_posres.gro -o GLC_1M_hIAPP.pdb

srun -N $SLURM_JOB_NUM_NODES -n $SLURM_NTASKS -c $OMP_NUM_THREADS -m block:block:block mdrun_mpi -s GLC_1M_hIAPP -deffnm GLC_1M_hIAPP -cpi -plumed plumed -multi 3 -replex 60000 &>> run.log -maxh 23.5
