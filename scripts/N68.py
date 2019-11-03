
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file_w = open('uwords','r')
file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'<h2 class="title">(?P<word>.+?)</h2>')

count = 0
i = 0
l = 0

unw = {}

for w in file_w:
	unw[w.strip('\n')] = '1'

for line in file:
	m = regex.match(line)
	if m:
		w = m.group('word')
		pl = unw.get(w.lower(),None)
		if pl != None:
			file_o.write(line)
			l += 1
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print("lines written = {} out of {}".format(l,count))