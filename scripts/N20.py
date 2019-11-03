
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

form = re.compile(r'{{en-(?P<form>.+?)\sof\|(?P<word>.+?)}}',re.IGNORECASE)

def repl(matchObj):
	t = matchObj.group('form').lower()
	w = matchObj.group('word')
	if t.startswith('comparative'):
		return "''comparative form of'' '''"+w+"''': more "+w
	elif t.startswith('past'):
		return "''simple past tense and past participle of'' '''"+w+"'''"
	elif t.startswith('simple past'):
		return "''simple past tense of'' '''"+w+"'''"
	else:
		return "''"+t+" of''"+" '''"+w+"'''"



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
