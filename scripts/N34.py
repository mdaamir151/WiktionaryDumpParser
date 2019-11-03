import place_data
import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{place\|.+?\|(?P<place>[^{]+?)}}',re.IGNORECASE) #taxonomical name

count = 0
i = 0
l = 0

def repl(matchObj):
	a = ''
	modern_name = ''
	capital = ''
	largest_city = ''
	caplc = ''
	article = ''
	t = []

	x = matchObj.group('place').split('|')
	arr = []
	s = ''
	comma = 0
	for item in x:
		if item.startswith('modern='):
			modern_name = item[len('modern='):].split(':')[-1]
		elif item.startswith('capital='):
			capital = item[len('capital='):].split(':')[-1]
		elif item.startswith('largest city='):
			largest_city = item[len('largest city='):].split(':')[-1]
		elif item.startswith('caplc='):
			caplc = item[len('caplc='):].split(':')[-1]
		elif item.startswith('a='):
			a = item[2:].split(':')[-1]
		elif re.match('t[0-9]=',item):
			t.append(item[3:].split(':')[-1])
		elif item == ';':
			arr[-1] += ';'
		elif item != '' and item.find('=') < 0:
			arr.append(item)

	val = ''
	for i in arr:
		if len(i.split('/')) == 2:
			sp = i.split('/')
			comma += 1
			if comma > 1:
				if s.strip()[-2:] not in ['of','in','at']: 
					s = s.strip()+', '
			val = sp[1]
		else:
			val = ' '.join(i.split('/'))
			comma = 0
		d = place_data.data.get(val,'')
		if type(d).__name__ == 'dict':
			art = d.get("article",'')
			if art != '':
				art += ' '
			prep = d.get('preposition','')
			if prep != '':
				prep = ' '+prep
			s +=  art + val.split(':')[-1] + prep + ' '
		elif d != '':
			s += d+' '+val.split(':')[-1] + ' '
		else:
			s += val.split(':')[-1] + ' '

	if a != '':
		article = a + ' '
	else:
		y = ''
		if len(arr[0].split('/')) == 2:
			y = arr[0].split('/')[0].strip()
			if y.split()[0] not in ['A','An','The','a','an','the']:
				article = 'An '+y+', ' if y[0] in ['A','E','I','O','U','a','e','i','o','u'] else 'A '+y+', '
			else:
				article = y + ' '
		else:
			article = 'An ' if s[0] in ['A','E','I','O','U','a','e','i','o','u'] else 'A '

	add_article = True

	if len(t) > 0:
		s = ', '.join(t)+' (' + s.strip() + ')'
		add_article = False
	
	if modern_name != '':
		s = s.strip() + '. Modern name: '+modern_name
	if largest_city != '':
		s = s.strip() + '. Largest city: '+largest_city
	if capital != '':
		s = s.strip() + '. Capital: '+capital
	if caplc != '':
		s = s.strip() + '. Capital and largest city: '+caplc

	if add_article:
		s = article + s.strip()

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