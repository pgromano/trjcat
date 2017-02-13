read -r -p "Name of file?: " name
xtc=${name}_proc.xtc
top=$(ls *.tpr | head -1)

# Get ordered times (Names should be labeled ${name}_${time}.xtc
# ${time} is the start time in ps of simulation chunk.

python set_time.py $name
gmx_mpi trjcat -f ${name}_*.xtc -o $xtc -settime < settime.inp
