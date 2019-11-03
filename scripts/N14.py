import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(qualifier|qual|q)\|(?P<nowrap>.+?)}}',re.IGNORECASE)
curLine = ''

def repl(matchObj):
	nowrap = matchObj.group('nowrap').split('|')
	return '('+nowrap[0]+')'


count = 0
i = 0
l = 0

for line in file:
	curLine = line
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))