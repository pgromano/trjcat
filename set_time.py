import numpy as np
from glob import glob
from sys import argv

file_template = str(argv[1])
N = len(file_template)+1

f = open('settime.inp', 'w')
files = sorted(glob('*.xtc'))
for file in files:
	f.write('%s\n' %file[N:-4])
f.close()
