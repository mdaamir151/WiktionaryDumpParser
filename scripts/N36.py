import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{ux\|(?P<example>.+?)}}')
curLine = ''

def repl(matchObj):
	example = matchObj.group('example').split('|')
	s = example[1]
	t = ''
	q = ''
	if len(example) > 2:
		index = example[2].find('=')
		if index > 0:
			t = example[2][index+1:]
		else:
			t = example[2]
	for item in example:
		if t == '' and item.startswith('t='):
			t = item[2:]
		elif t == '' and item.startswith('translation='):
			t = item[len('translation='):]
		elif item in ['q=','q1=','qualifier=','qualifier1=']:
			index = item.find('=')
			q = item[index+1:]
	if q != '':
		s += ' ('+q+')'
	if t != '':
		index = curLine.find(' ')
		s = s+'\n'+curLine[:index+1]+t
	return "''"+s+"''"


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