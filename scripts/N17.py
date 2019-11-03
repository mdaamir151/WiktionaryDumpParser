
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

sense = re.compile(r'{{(ant|antonym|antonyms)\|.+?\|(?P<ant>.+?)}}',re.IGNORECASE)

def repl(matchObj):
	antonyms = []
	qualifier = {}
	m = matchObj.group('ant').split('|')
	for i in m:
		if i.find('=') < 0:
			antonyms.append(i)
		elif i.startswith('q'):
			index = i.find('=')
			qualifier[i[1:index]] = i[index+1:]
	s = ''
	for i in range(len(antonyms)):
		s += antonyms[i]
		q = qualifier.get(str(i+1),None)
		if q != None:
			s += "(''"+q+"'')"
		s += ', '
	if s != '':
		return "''Antonyms:'' "+s[:-2]
	else:
		return ''



count = 0
i = 0
l = 0

for line in file:
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
	line = sense.sub(repl,line)
	file_o.write(line)


print('{} lines processed'.format(count))
