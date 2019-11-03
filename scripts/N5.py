
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'\[\[(w:|wikipedia:|wiktionary:|wikt:|wikisource:|s:|w\||wikipedia\||wiktionary\||wikt\||wikisource\||s\|)(?P<link>.+?)\]\]')
regex2 = re.compile(r'{{(w:|wikipedia:|wiktionary:|wikt:|wikisource:|s:|w\||wikipedia\||wiktionary\||wikt\||wikisource\||s\|)(?P<link>.+?)}}')

count = 0
i = 0
l = 0

def repl(matchObj):
	link = matchObj.group('link').split('|')
	if len(link) == 1:
		return link[0]
	elif len(link) > 1:
		j = len(link) - 1
		while j >= 0:
			if link[j].find('=') < 0:
				return link[j]
			j -= 1
	return ''



for line in file:
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
	line = regex.sub(repl,line)
	line = regex2.sub(repl,line)
	file_o.write(line)
print('{} lines written out of {}'.format(count,count))
