import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(l|ll|link|l-self|m|mention|m-self)\|(?P<link>.+?)}}')

def repl(matchObj):
	link = matchObj.group('link').split('|')
	ln = len(link)-1
	s = ''
	while ln >= 0:
		if link[ln].startswith('t='):
			s += link[ln][2:]+','
		elif len(link[ln]) > 2 and link[ln] != 'mul' and link[ln].find('=') < 0:
			s += link[ln]
			return s
		ln -= 1
	return s

count = 0
i = 0
l = 0

for line in file:
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))