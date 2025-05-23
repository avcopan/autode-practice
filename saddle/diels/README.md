To run ORCA in parallel, you need to make sure you have `mpirun` in your path from
OpenMPI 4.1.1, and that `orca` is an alias referring to the absolute path to the orca
executable:
```
module load orca/5.0.4
module load openmpi/4.1.1
alias orca=$(which orca)
```
