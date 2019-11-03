import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(.+?)}}')
syn = re.compile(r'=+antonym.+?',re.IGNORECASE)

count = 0
i = 0
l = 0
write = True
synonym = []

for line in file:
	if syn.match(line):
		if write:
			file_o.write(line)
			l += 1
		write = False
	elif (not write) and (line.startswith('=') or line.startswith('<title>')):
		s = ', '.join(synonym)
		if len(synonym) > 0:
			file_o.write('* '+s.strip().strip(',')+'\n')
			l += 1
		synonym = []
		write = True
	if write:
		file_o.write(line)
		l += 1
	else:
		matches = regex.findall(line)
		if len(matches) > 1 and matches[0].startswith('sense'):
			s = '\'\'(' + matches[0].split('|')[-1] + ')\'\' : '
			arr = []
			for i in range(1,len(matches)):
				spl = matches[i].split('|')
				if len(spl) < 3:
					continue
				if spl[0] == 'l' and spl[1] == 'en':
					arr.append(spl[-1])
			s += ', '.join(arr)
			file_o.write('* '+s.strip().strip(',')+'\n')
			l += 1
		elif len(matches) > 0:
			for item in matches:
				spl = item.split('|')
				if len(spl) > 2 and spl[0] == 'l' and spl[1]=='en':
					synonym.append(spl[-1])
		
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {}'.format(l,count))
