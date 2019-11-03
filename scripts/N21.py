
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

form = re.compile(r'{{(?P<form>[a-zA-Z\s-]+?)\sof\|(?P<word>.+?)}}',re.IGNORECASE)

def repl(matchObj):
	t = matchObj.group('form')
	w = matchObj.group('word').split('|')
	if len(w) > 0:
		for i in w:
			if i.find('=') < 0:
				return "''"+t+" of''"+" '''"+i+"'''"
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
	line = form.sub(repl,line)
	file_o.write(line)


print('{} lines processed'.format(count))
