import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(en-adj|en-adjective|en-adv|en-adverb)(\|)?(?P<adjv>.*?)}}')
hw = re.compile(r'<title>(?P<headword>.+?)</title>')
sup = re.compile(r'sup[0-9]*?=')
headword = ''

def repl(matchObj):
	if matchObj:
		adjv = matchObj.group('adjv').split('|')
	else:
		adjv = []
	comparative = ''
	superlative = ''
	head = headword
	incomparable = ''
	comparativeOnly = ''
	morefurther = ''
	nosuperlative = True

	for it in adjv:
		if sup.match(it) and it.find('=') >= 0:
			nosuperlative = False
			break

	for item in adjv:
		if item == 'more':
			comparative = comparative+" ''or'' " + (item + ' ' +headword) if comparative != '' else (item + ' ' +headword)
			superlative = superlative+" ''or'' " + ('most'+ ' ' +headword) if superlative != '' else ('most'+ ' ' +headword)
			morefurther = 'mf'
		elif item == 'further':
			comparative = comparative+" ''or'' " + (item + ' ' +headword) if comparative != '' else (item + ' ' +headword)
			superlative = superlative+" ''or'' " + ('furthest'+ ' ' +headword) if superlative != '' else ('furthest'+ ' ' +headword)
			morefurther = 'mf'
		elif item == 'er':
			if headword.endswith('ey'):
				comparative = comparative+" ''or'' " + (headword[:-2]+'ier') if comparative != '' else (headword[:-2]+'ier') 
				superlative = superlative+" ''or'' " + (headword[:-2]+'iest') if superlative != '' else (headword[:-2]+'iest')
			elif headword.endswith('y'):
				comparative = comparative+" ''or'' " + (headword[:-1]+'ier') if comparative != '' else (headword[:-1]+'ier')
				superlative = superlative+" ''or'' " + (headword[:-1]+'iest') if superlative != '' else (headword[:-1]+'iest')
			elif headword.endswith('e'):
				comparative = comparative+" ''or'' " + (headword[:-1]+'er') if comparative != '' else (headword[:-1]+'er')
				superlative = superlative+" ''or'' " + (headword[:-1]+'est') if superlative != '' else (headword[:-1]+'est')
			else:
				comparative = comparative+" ''or'' " + (headword+'er') if comparative != '' else (headword+'er')
				superlative = superlative+" ''or'' " + (headword+'est') if superlative != '' else (headword+'est')
		elif item.startswith('h=') or item.startswith('head='):
			index = item.find('=')
			head = item[index+1:]
		elif item.startswith('sup'):
			index = item.find('=')
			if index >= 0:
				superlative = superlative+" ''or'' " + (item[index+1:]) if superlative != '' else (item[index+1:])
		elif item == '-':
			incomparable = '-'
		elif item == '+':
			comparativeOnly = '+'
		elif item.find('=') < 0 and item != '':
			comparative = comparative+" ''or'' " + (item) if comparative != '' else (item)
			if item.endswith('er') and nosuperlative:
				superlative = superlative+" ''or'' " + (item+'est') if superlative != '' else (item+'est')

	s = ''
	if comparativeOnly != '':
		s =  "comparative only'')"
	elif len(adjv) == 1 and adjv[0] == '' and comparative == '':
		s = "comparative'' more "+headword+", ''superlative'' most "+headword+")"
	elif comparative != '':
		s = "comparative'' "+comparative+", "+"''superlative'' "+superlative+")"

	if incomparable != '' and s != '':
		s = "'''"+head+"''' (''usually not comparable, "+s
	elif incomparable != '':
		s = "'''"+head+"''' (''not comparable)''"
	elif s != '':
		s = "'''"+head+"''' (''"+s
	else:
		s = "'''"+head+"'''"

	return s


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