
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

sense = re.compile(r'{{(syn|synonym|synonyms)\|.+?\|(?P<syn>.+?)}}',re.IGNORECASE)

def repl(matchObj):
	synonyms = []
	qualifier = {}
	m = matchObj.group('syn').split('|')
	for i in m:
		if i.find('=') < 0:
			synonyms.append(i)
		elif i.startswith('q'):
			index = i.find('=')
			qualifier[i[1:index]] = i[index+1:]
	s = ''
	for i in range(len(synonyms)):
		s += synonyms[i]
		q = qualifier.get(str(i+1),None)
		if q != None:
			s += "(''"+q+"'')"
		s += ', '
	if s != '':
		return "''Synonyms:'' "+s[:-2]
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
