
import re

fin = open("N73.html",'r')
fout = open("out.html",'w')

word = re.compile(r"<(?P<tag>[a-zA-Z0-9]+?)></\1>")

count = 0
l = 0
i = 0

for line in fin:
	if word.search(line):
		fout.write(line)
		l += 1
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {} lines'.format(l,count))