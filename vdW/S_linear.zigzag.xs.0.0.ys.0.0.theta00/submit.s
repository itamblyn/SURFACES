#! /bin/bash
#$ -N rotator 
#$ -S /bin/bash
##$ -M isaac.tamblyn@nrc.ca
#$ -m bea
#---->> (-pe = Number of nodes to use)
#$ -pe dev 8 
#---->> (res_cpus = Number of CPUs/node)
#$ -l res_cpus=16
#---->> (rec_mem = memory / node (MB))
#$ -l res_mem=16000
#$ -l res_image=nrc_all_default_ubuntu-14.04-amd64_1.3

#---->> CASE_DIR is the directory where the job should run
CASE_DIR=/home/ist001/work/bnnt/surfaces/rotator/vdW/S_linear.zigzag.xs.0.0.ys.0.0.theta00

#---->> Ensure that is matches the line above...
#$ -wd /home/ist001/work/bnnt/surfaces/rotator/vdW/S_linear.zigzag.xs.0.0.ys.0.0.theta00


. ssmuse-sh -d main/opt/intelcomp/intelcomp-2016.1.156/
. ssmuse-sh -d main/opt/openmpi/openmpi-1.6.5/intelcomp-2016.1.156
. ssmuse-sh -p nrc/sdt/vasp/vasp_5.4.1_ubuntu-14.04-x86-64

cd $CASE_DIR
sleep 10
rumpirun -wdir $CASE_DIR -np 128  $VASP_PATH/vasp_std > log
