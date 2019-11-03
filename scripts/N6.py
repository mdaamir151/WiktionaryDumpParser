
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

# should contain quotes as examples for better understanding
# check wares doesn't have pronunciation entry after running this
#can include audio, hyphenation, rhyme words, etc.

regex = re.compile(r'/.+?/')
pronun = re.compile(r'^=+Pronunciation',re.IGNORECASE)
unselect = re.compile(r'//|[\{\},\|=\?\s&;0-9]+?')

count = 0
i = 0
l = 0
write = True
pronunciation = []

for line in file:
	if pronun.match(line) and write:
		file_o.write(line)
		l += 1
		write = False
	elif (not write) and (line.startswith('=') or line.startswith('<title>')):
		s = ', '.join(pronunciation)
		file_o.write('* '+s+'\n')
		pronunciation = []
		l += 1
		write = True
	if write:
		file_o.write(line)
		l += 1
	else:
		matches = regex.findall(line)
		# remove links
		for m in matches:
			if unselect.search(m) is None:
				pronunciation.append(m)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {}'.format(l,count))
