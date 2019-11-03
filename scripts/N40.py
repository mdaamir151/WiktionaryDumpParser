import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(en-plural noun)(\|)?(?P<singular>.*?)}}')
hw = re.compile(r'<title>(?P<headword>.+?)</title>')
headword = ''

def repl(matchObj):
	singular = matchObj.group('singular').split('|')
	sg = ''
	head = headword
	for item in singular:
		if item.startswith('head=') or item.startswith('Head='):
			head = item[len('head='):]
		elif item.startswith('sg='):
			sg = item[len('sg='):]
			

	if sg == '':
		return "'''"+head+"''' (''plural only'')"
	else:
		return "'''"+head+"''' (''usually plural;'' singular"+sg+")"



count = 0
i = 0
l = 0

for line in file:
	m = hw.match(line)
	if m:
		headword = m.group('headword')
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))