#!/bin/bash
#
# ===================================================
# ITEM 3
#
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
# 
# Last modification: 02/15/2024
# Version: 1.0
# ===================================================
#
#SBATCH -J job_int_study 
#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p compute1          # Queue (partition) name.
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 1                 # Total number of tasks to be requested.
#SBATCH -c 80                # Number of processors used by each task.
#SBATCH -t 00:30:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user sara.restrepovelasquez2@my.utsa.edu  # Put your utsa-email here.

module load anaconda3
conda activate envTeam7

i_array=(1 2 4 8)

for i in ${i_array[@]} 
do
	export OMP_NUM_THREADS=$i
	export NUMEXPR_NUM_THREADS=$i
        python3 integral.py
done 
