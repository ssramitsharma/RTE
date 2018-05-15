#!/bin/bash
#PBS -q hpc1
#PBS -l walltime=1:10:00
#PBS -l nodes=2:ppn=32
#PBS -l vmem=100gb

# following the actions to be performed by the job
# start here your MPI program on the nodes we got assigned from the batch system

module load cuda
module load opencl/nvidia
export OMP_NUM_THREADS=4

cd Entailmentlstm/
python Entailmentlstm.py 
