import place_data
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{[^{]+?}}') 

count = 0
i = 0
l = 0

for line in file:
	line = regex.sub('',line)
	file_o.write(line)
	count += 1

print('{} lines written out of {}'.format(count,count))
