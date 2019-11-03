import os
import re

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+"_0.xml","w",buffering=1,encoding='utf-8')

word = re.compile(r"<(?P<tag>[a-zA-Z0-9]+?)></\1>")

count = 0
l = 0
i = 0

for line in file:
	line = word.sub('',line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {} lines'.format(count,count))

file.close()
file_o.close()
file = open("N"+str(outseq)+"_0.xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".html","w",buffering=1,encoding='utf-8')
count = 0
for line in file:
	line = word.sub('',line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print('{} lines written out of {} lines'.format(count,count))