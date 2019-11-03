import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'<h2 class="title">(?P<word>.+?)</h2>')

count = 0
i = 0
l = 0

unw = {}

for line in file:
	m = regex.match(line)
	if m:
		w = m.group('word')
		pl = unw.get(w.lower(),None)
		if pl == None:
			unw[w.lower()] = line
			l += 1
		else:
			pw = regex.match(pl).group('word')
			if w > pw:
				unw[w.lower()] = line

	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
for k,v in unw.items():
	file_o.write(v)
print("lines written = {} out of {}".format(l,count))