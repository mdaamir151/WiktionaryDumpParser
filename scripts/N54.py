import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'\'\'(?P<g>.+?)\'\'')
example = re.compile(r'(?P<n>#+?:\s)\'\'.+\'$')

def repl(matchObj):
	m = matchObj.group('g')
	return '<span class="italics">'+m+"</span>"

count = 0
i = 0
l = 0

for line in file:
	m = example.match(line)
	if m:
		ln = len(m.group('n'))
		st = line[:ln]
		line = line[ln:].strip('\n').strip().strip("''")
		line = st+'<span class="ex-italics">'+line+'</span>'+'\n'
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))