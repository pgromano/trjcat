# trjcat
Bash/Python script to automate concatenation of multiple **GROMACS** trajectory files. Assumes trajectories are named with the specific template `${NAME}_${TIME}.xtc`. Here, `${NAME}` would be the template name for all simulations, and `${TIME}$` would be the timestamp for the *start* of the simulation chunk.

### Running
For a several trajectory files name TRAJ_*.xtc

	sh process.sh < "TRAJ"
