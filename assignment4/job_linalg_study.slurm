#!/bin/bash
#
# =================
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
# Last modification: 02/16/2024
# Version 1.0
# =================
#
# Definition of the SLURM configuration:
#
#SBATCH -J job_linalg_study
#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of threads used by each task.
#SBATCH -t 00:05:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user dainam.nguyen@my.utsa.edu # Put your utsa-email here.
#
#
# Load Anaconda3 to be able to access the specific environment.
ml anaconda3

# Acivate the environment
conda activate envTeam7


for i in 1 2 4 8 16 20 40;
do
	export MKL_NUM_THREADS=$i
	echo $MKL_NUM_THREADS
	srun --exclusive -J run$i -N1 -n1 -c $SLURM_CPUS_PER_TASK python3 linalg.py &
	wait
done



