import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{head\|?(?P<head>.*?)}}')
hw = re.compile(r'<title>(?P<headword>.+?)</title>')

headword = ''

def repl(matchObj):
	header = matchObj.group('head').split('|')
	if len(header) < 3:
		return "'''"+headword+"'''"
	
	header = header[2:]
	head = headword

	arr = []

	for item in header:
		if item.startswith('head=') or item.startswith('Head='):
			head = item[len('head='):]
		elif item == 'and' or item == 'or':
			arr[-1] += ' '+item+' '
		elif item =='' or item == ' ':
			arr.append('')
		elif item.find('=') < 0:
			if len(arr) > 0 and arr[-1].endswith(' '):
				arr[-1] += item
			else:
				arr.append(item)

	arr2 = []

	for i in range(int(len(arr)/2)):
		arr2.append(arr[2*i]+' '+arr[2*i+1])

	s = ', '.join(arr2)

	if s == '':
		return "'''"+head+"'''"

	return "'''"+head+"''' "+'('+s+')'

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