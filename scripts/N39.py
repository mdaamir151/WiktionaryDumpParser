import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(en-proper noun|en-prop)(\|)?(?P<plural>.*?)}}')
hw = re.compile(r'<title>(?P<headword>.+?)</title>')
headword = ''

def repl(matchObj):
	plural = matchObj.group('plural').split('|')
	uncountable = False
	countAndUncount = False
	noplural = False

	if '-' in plural:
		uncountable = True
		plural.remove('-')
	elif '~' in plural:
		countAndUncount = True
		plural.remove('~')
	if '!' in plural:
		plural.remove('!')
		noplural = True
	if '?' in plural:
		plural.remove('?')
		noplural = True

	mult = ''

	head = headword
	for item in plural:
		if item.startswith('head=') or item.startswith('Head='):
			head = item[len('head='):]
		elif item == 's' or item == 'es':
			mult = mult + ' or '+(headword+item) if mult != '' else (headword+item)
		elif item != '':
			mult = mult + ' or '+(item) if mult != '' else (item)

	if noplural:
		return "'''"+head+"'''"
	elif uncountable and mult != '':
		return "'''"+head+"''' (''usually uncountable; plural'' "+mult+")"
	elif countAndUncount and mult != '':
		return "'''"+head+"''' (''countable and uncountable; plural'' "+mult+")"
	else:
		return "'''"+head+"'''"



count = 0
i = 0
l = 0

for line in file:
	m = hw.match(line)
	if m:
		headword = m.group('headword')
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))