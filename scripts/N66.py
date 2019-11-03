
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{color panel\|(?P<tax>[^{]+?)}}',re.IGNORECASE)
headword = re.compile(r'<h2 class="title">(?P<head>.+?)</h2>')

count = 0
i = 0
l = 0
head = ''

def repl(matchObj):
	m = matchObj.group('tax').split('|')
	c = ''
	if len(m) == 2:
		return m[0]+' : '+'<i style="background-color:#'+m[1]+'" class="color-panel"></i>'
	if len(m) == 1:
		return head+' : '+'<i style="background-color:#'+m[0]+'" class="color-panel"></i>'
	return ''

for line in file:
	m = headword.match(line)
	if m:
		head = m.group('head')
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {}'.format(count,count))
