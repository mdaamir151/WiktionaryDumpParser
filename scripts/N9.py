
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{rf|{{delete|{{gloss-stub|{{t-need|{{subst|{{w\||{{wiki')

count = 0
i = 0
l = 0

for line in file:
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
	if not regex.search(line):
		file_o.write(line)
		l += 1
print('{} lines written out of {}'.format(l,count))
