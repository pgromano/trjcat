import numpy as np
from glob import glob

f = open('settime.inp', 'w')
files = sorted(glob('*.xtc'))
for file in files:
	f.write('%sn; % file[4:-4])
f.close()
