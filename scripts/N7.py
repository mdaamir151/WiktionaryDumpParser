import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'\[\[(?P<repl>.+?)\]\]')
links = re.compile(r':')
count = 0
i = 0
selected = False
num_lines = 0

def replacementString(matchObj):
	if links.search(matchObj.group('repl')):
		return ''
	elif len(matchObj.group('repl').split('|')) > 1:
		return matchObj.group('repl').split('|')[1]
	else:
		return matchObj.group('repl')


for line in file:
	l = regex.sub(replacementString,line)
	file_o.write(l)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))