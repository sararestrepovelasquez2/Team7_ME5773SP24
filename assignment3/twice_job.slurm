#!/bin/bash
#
# =================
# ITEM 5
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
# Last modification: 02/08/2024
# Version 1.0
# =================
#
# Definition of the SLURM configuration:
#
#SBATCH -J twice_job
#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p amdonly           # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 4                 # Total number of tasks to be requested.
#SBATCH -c 8                 # Number of threads used by each task.
#SBATCH -t 00:12:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user sara.restrepovelasquez2@my.utsa.edu # Put your utsa-email here.
#
t_start=$(date +%s) # Start time
#
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 5 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 2 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 7 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 6 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 1 &
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 3 &
#
wait # Waiting for all executions to complete before proceeding.  
#
t_end=$(date +%s) # End time
runtime=$((t_end-t_start)) # Total time
#
echo The runtime for this job was $runtime [s].
