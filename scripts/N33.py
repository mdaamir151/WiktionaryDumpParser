
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{short (of|for)\s?\|(?P<tax>[^{]+?)}}',re.IGNORECASE) #taxonomical name

count = 0
i = 0
l = 0

def repl(matchObj):
	m = matchObj.group('tax').split('|')
	arr = []
	for i in m:
		if i.find('=') < 0 and len(i) > 3: # skip language code like en
			arr.append(i)
	if len(arr) == 1:
		return "''short for'' "+arr[0]
	elif len(arr) > 1:
		return "''short for'' "+arr[0]+" ("+arr[1]+")"
	return ''

for line in file:
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {}'.format(count,count))