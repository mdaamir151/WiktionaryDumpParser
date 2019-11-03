import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{(en-verb)(\|)?(?P<verb>.*?)}}')
hw = re.compile(r'<title>(?P<headword>.+?)</title>')

pres_3sg = re.compile(r'pres_3sg(?P<m>[0-9]?)=')
pres_3sg_qual = re.compile(r'pres_3sg(?P<m>[0-9]?)_qual=')
pres_ptc = re.compile(r'pres_ptc(?P<m>[0-9]?)=')
pres_ptc_qual = re.compile(r'pres_ptc(?P<m>[0-9]?)_qual=')
past = re.compile(r'past(?P<m>[0-9]?)=')
past_qual = re.compile(r'past(?P<m>[0-9]?)_qual=')
past_ptc = re.compile(r'past_ptc(?P<m>[0-9]?)=')
past_ptc_qual = re.compile(r'past_ptc(?P<m>[0-9]?)_qual=')

headword = ''

def repl(matchObj):
	verb = matchObj.group('verb').split('|')
	v = []
	tps = ''
	tpse = []
	ftpse = ''
	tpsq = {}
	pr_ptc = ''
	pr_ptce = []
	fpr_ptce = ''
	pr_ptcq = {}
	sp = ''
	spe = []
	fspe = ''
	spq = {}
	pa_ptc = ''
	pa_ptce = []
	fpa_ptce = ''
	pa_ptcq = {}

	stem = ''
	head = headword

	for item in verb:
		if item == '':
			continue
		if item.find('=') < 0:
			v.append(item)
			continue
		elif item.startswith('head=') or item.startswith('Head='):
			head = item[len('head='):]
			continue
		val = item[item.find('=')+1:]
		if pres_3sg.match(item):
			tpse.append(val)
		elif pres_3sg_qual.match(item):
			m = pres_3sg_qual.match(item)
			if m.group('m') == '':
				ftpse = '('+val+')'
			else:
				tpsq[int(m.group('m'))] = val
		elif pres_ptc.match(item):
			pr_ptce.append(val)
		elif pres_ptc_qual.match(item):
			m = pres_ptc_qual.match(item)
			if m.group('m') == '':
				fpr_ptce = '('+val+')'
			else:
				pr_ptcq[int(m.group('m'))] = val
		elif past.match(item):
			spe.append(val)
		elif past_qual.match(item):
			m = past_qual.match(item)
			if m.group('m') == '':
				fspe = '('+val+')'
			else:
				spq[int(m.group('m'))] = val
		elif past_ptc.match(item):
			pa_ptce.append(val)
		elif past_ptc_qual.match(item):
			m = past_ptc_qual.match(item)
			if m.group('m') == '':
				fpa_ptce = '('+val+')'
			else:
				pa_ptcq[int(m.group('m'))] = val

	for i in range(len(tpse)):
		if tpsq.get(2+1,None) != None:
			x = tpsq.get(i+2,None)
			tpse[i] += '('+x+')'
	for i in range(len(pr_ptce)):
		if pr_ptcq.get(i+2,None) != None:
			x = pr_ptcq.get(i+2,None)
			pr_ptce[i] += '('+x+')'
	for i in range(len(spe)):
		if spq.get(i+2,None) != None:
			x = spq.get(i+2,None)
			spe[i] += '('+x+')'
	for i in range(len(pa_ptce)):
		if pa_ptcq.get(i+2,None) != None:
			x = pa_ptcq.get(i+2,None)
			pa_ptce[i] += '('+x+')'

	e1 =" ''or'' ".join(tpse)
	e2 =" ''or'' ".join(pr_ptce)
	e3 =" ''or'' ".join(spe)
	e4 =" ''or'' ".join(pa_ptce)

	s = []

	s1 = "''third-person singular simple present'' "
	s2 = "''present participle'' "
	s3 = "''simple past and past participle'' "


	if len(v) > 2:
		tps = v[0]
		pr_ptc = v[1]
		sp = v[2]
	if len(v) > 3:
		pa_ptc = v[3]

	if 'es' in v:
		stem = headword
		if v[0] != 'es':
			if v[1] != 'es':
				stem = v[0]+v[1]
			else:
				stem = v[0]
		tps = stem + 'es'
		pr_ptc = headword + 'ing'
		sp = headword + 'ed'
	elif 'ies' in v:
		stem = headword
		if v[0] != 'ies':
			if v[1] != 'ies':
				stem = v[0]+v[1]
			else:
				stem = v[0]
		tps = stem + 'ies'
		pr_ptc = headword + 'ing'
		sp = stem + 'ied'
	elif 'd' in v:
		stem = headword
		if v[0] != 'd':
			if v[1] != 'd':
				stem = v[0]+v[1]
			else:
				stem = v[0]
		tps = headword + 's'
		pr_ptc = headword + 'ing'
		sp = stem + 'd'
	elif 'ing' in v:
		stem = headword
		if v[0] != 'ing':
			if v[1] != 'ing':
				stem = v[0]+v[1]
			else:
				stem = v[0]
		tps = headword + 's'
		pr_ptc = stem + 'ing'
		sp = stem + 'ed'

	if 'es' in v or 'd' in v or 'ies' in v or 'ing' in v or len(v) == 3:
		s = []
		s1 = s1 + tps + ftpse if e1 == '' else s1 + tps + ftpse + " ''or'' " + e1
		s.append(s1)
		s2 = s2 + pr_ptc + fpr_ptce if e2 == '' else s2 + pr_ptc + fpr_ptce + " ''or'' " + e2
		s.append(s2)
		s3 = s3 + sp + fspe if e3 == '' else s3 + sp + fspe + " ''or'' " + e3
		s.append(s3)

		return "'''"+head+"''' ("+', '.join(s)+")"

	if len(v) > 3:
		s = []
		s3 = "''simple past'' "
		s4 = "''past participle'' "
		s1 = s1 + tps + ftpse if e1 == '' else s1 + tps + ftpse + " ''or'' " + e1
		s.append(s1)
		s2 = s2 + pr_ptc + fpr_ptce if e2 == '' else s2 + pr_ptc + fpr_ptce + " ''or'' " + e2
		s.append(s2)
		s3 = s3 + sp + fspe if e3 == '' else s3 + sp + fspe + " ''or'' " + e3
		s.append(s3)
		s4 = s4 + pa_ptc + fpa_ptce if e4 == '' else s4 + pa_ptc + fpa_ptce + " ''or'' " + e4
		s.append(s4)

		return "'''"+head+"''' ("+', '.join(s)+")"

	if len(v) == 0 or len(v) == 1:
		if len(v) == 1:
			stem = v[0]
		else:
			stem = headword
		s1 = s1 + (headword+'s') + ftpse if e1 == '' else s1 + (headword+'s') + ftpse + " ''or'' " + e1
		s.append(s1)
		s2 = s2 + (stem+'ing') + fpr_ptce if e2 == '' else s2 + (stem+'ing') + fpr_ptce + " ''or'' " + e2
		s.append(s2)
		s3 = s3 + (stem+'ed') + fspe + fpa_ptce if e3 == '' else s3 + (stem+'ed') + fspe + fpa_ptce + " ''or'' " + e3
		s.append(s3)

		return "'''"+head+"''' ("+', '.join(s)+")"

	return ''


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