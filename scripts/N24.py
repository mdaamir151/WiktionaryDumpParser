import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

count = 0
i = 0
l = 0
s = ''

for line in file:
	if s != '' and not line.startswith('</'):
		file_o.write(s+'\n')
		s = line[:-1]
		l += 1
	else:
		s += line[:-1]
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(l,count))