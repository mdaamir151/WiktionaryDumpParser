
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

form = re.compile(r'{{form of\|(?P<form>.+?)}}',re.IGNORECASE)

def repl(matchObj):
	m = matchObj.group('form').split('|')
	s = ''
	if len(m) > 3:
		s = "''"+m[0]+" of'' "+m[2]
	else:
		s = "''"+m[0]+" of'' "+m[1]
	return s



count = 0
i = 0
l = 0

for line in file:
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
	line = form.sub(repl,line)
	file_o.write(line)


print('{} lines processed'.format(count))
