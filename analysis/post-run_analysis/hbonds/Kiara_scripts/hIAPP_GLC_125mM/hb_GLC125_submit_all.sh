#!/bin/bash --login
#SBATCH --partition=debug
#SBATCH --job-name="hb_All_GLC125"
#SBATCH --time=1:00:00
#SBATCH --account=pawsey0110
#SBATCH --ntasks=10
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --mem=120G
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

#Only need command below for MPI jobs (then repeat before each subsequent srun command)
export FI_CXI_DEFAULT_VNI=$(od -vAn -N4 -tu < /dev/urandom)

#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_MCNH_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_MCNH_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_MCNH_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_MCNH_water_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_MCO_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_MCO_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_MCO_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_MCO_water_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_osmo_osmo_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_osmo_osmo_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_osmo_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_osmo_water_GLC125_hIAPP.out 2>&1 &
srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_pro_pro_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_pro_pro_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_sc_osmo_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_sc_osmo_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_sc_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_sc_water_GLC125_hIAPP.out 2>&1 &
#srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_water_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_water_water_GLC125_hIAPP.out 2>&1 &
srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_pro_osmo_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_pro_osmo_GLC125_hIAPP.out 2>&1 &
srun -N $SLURM_JOB_NUM_NODES -n 1 -c 1 --mem=12G ./hb_pro_water_GLC125_hIAPP.sh > slurm-"$SLURM_JOB_ID"_hb_pro_water_GLC125_hIAPP.out 2>&1 &

wait
