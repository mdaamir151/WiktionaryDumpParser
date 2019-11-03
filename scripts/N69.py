
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{place:(?P<tax>[^{]+?)}}',re.IGNORECASE)

count = 0
i = 0
l = 0

def repl(matchObj):
	m = matchObj.group('tax').split('|')

	region = ''
	capital = ''
	state = ''
	country = ''
	base = ''
	
	for item in m:
		if item.startswith('region='):
			region = item[len('region='):]
		elif item.startswith('capital='):
			capital = item[len('capital='):]
		elif item.startswith('state='):
			state = item[len('state='):]

	sp = m[0].split(r'/')
	base = m[0]
	if len(sp) > 1:
		country = sp[0]
		base = sp[1]
	elif m[0].find('of') > 0:
		index = m[0].find('of')
		country = m[0][index+3:]
		base = m[0][:index-1]

	if base == 'state':
		s = country if region == '' else region + ' of ' + country
		if capital != '':
			s += '. Capital: ' + capital +'.'
		return 'A state in ' + s

	if base == 'state capital':
		s = 'A municipality, the capital of the state of ' + state + ', ' + country + '.'
		if capital != '':
			s += '. Capital: ' + capital +'.'
		return s

	if base == 'municipality':
		s = 'A municipality of the state of ' + state + ', ' + country + '.'
		if capital != '':
			s += '. Capital: ' + capital +'.'
		return s

	s = 'The ' + base + ' of ' + country
	if capital != '':
			s += '. Capital: ' + capital +'.'	 
	return s

for line in file:
	line = regex.sub(repl,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0

print('{} lines written out of {}'.format(count,count))
