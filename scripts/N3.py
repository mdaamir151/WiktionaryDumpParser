
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

count = 0
i = 0
selected = False
num_lines = 0

for line in file:
	if line[0] == '<':
		selected = False
		if line.startswith('<title>'):
			file_o.write(line)
			num_lines += 1
	elif line.startswith('==English=='):
		selected = True
	elif line.startswith('==') and line[2] != '=':
		selected = False
	if selected:
		file_o.write(line)
		num_lines += 1
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(num_lines,count))