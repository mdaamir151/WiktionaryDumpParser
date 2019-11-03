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
firstTime = True

for line in file:
	if line.startswith('## '):
		if firstTime:
			line = '<ol>'+'\n'+'<li>'+line.strip('\n')[3:]+'</li>'+'\n'
			firstTime = False
		else:
			line = '<li>'+line.strip('\n')[3:]+'</li>'+'\n'
	elif line.startswith('<li>') or line.startswith('<h') or line.startswith('<title') or line.startswith('</') or line.startswith('<ol'):
		if not firstTime:
			line = '</ol>'+'\n'+line
			firstTime = True

	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))