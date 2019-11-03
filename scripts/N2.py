
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

count = 0
i = 0

for line in file:
	if line.startswith('<text'):
		index = line.find('==English==')
		if index > -1:
			line = line[:index]+os.linesep+line[index:]
	
	file_o.write(line)

	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print(str(count)+" lines processed")