import numpy as np
from glob import glob
from sys import argv

file_template = str(argv[1])
N = len(file_template)

f = open('settime.inp', 'w')
files = sorted(glob('*.xtc'))
for file in files:
	f.write('%sn; % file[N:-4])
f.close()
