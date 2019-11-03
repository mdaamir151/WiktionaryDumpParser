
#{{nowrap|....}} inside {{lb|....}} and {{ux|....}} error

mp = open('contextMap.data','r')
st = {}
for line in mp:
	kv = line.strip().strip('\n').split(':')
	if len(kv) > 1:
		st[kv[0].lower()] = kv[1]

import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(lb|lbl|label)\|(?P<label>.+?)}}')

def repl(matchObj):
	label = matchObj.group('label').split('|')
	s = ''
	for items in label:
		item = items.strip().lower()
		if item == 'en':
			continue
		elif item == '_':
			s += ' '
		elif item == 'and' or item == 'or':
			s += ' '+item+' '
		elif item == 'chiefly' or item == 'of a':
			if len(s) == 0 or s[-1] == ' ':
				s += item + ' '
			else:
				s += ', '+item +' '
		elif st.get(item,None) != None:
			if len(s) == 0 or s[-1] == ' ':
				s += st.get(item)
			else:
				s += ', '+st.get(item)
		else:
			if len(s) == 0 or s[-1] == ' ':
				s += item
			else:
				s += ', '+item
	if s == '':
		return ''
	return '('+"''"+s.strip().strip(',')+"''"+')'

count = 0
i = 0
l = 0

for line in file:
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))