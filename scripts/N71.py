import place_data
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'<h2 class="title">(?P<word>.+?)</h2>')

dc = {}

count = 0
i = 0
l = 0

print("reading...")
for line in file:
	word = regex.match(line).group('word')
	dc[word] = line
	count += 1

sorted_words = sorted(dc.items())
print("writing...")
for (k,v) in sorted_words:
	file_o.write(v)
	l += 1

print('{} lines written out of {}'.format(l,count))
