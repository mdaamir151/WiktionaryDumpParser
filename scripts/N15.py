
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

senseid = re.compile(r'{{senseid.+?}}')
sense = re.compile(r'{{sense\|(?P<sense>.+?)}}')

count = 0
i = 0
l = 0

for line in file:
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
	line = sense.sub(r"''(\g<sense>):''",line)
	line = senseid.sub('',line)
	file_o.write(line)


print('{} lines processed'.format(count))
