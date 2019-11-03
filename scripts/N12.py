import re
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

regex = re.compile(r'{{defdate.+?}}')
bold = re.compile(r'(?P<one>{{.*?)\'\'\'(?P<bold>.+?)\'\'\'(?P<two>.*?}})')
italics = re.compile(r'(?P<three>{{.*?)\'\'(?P<italics>.+?)\'\'(?P<four>.*?}})')

def replBold(matchObj):
	s = matchObj.group('bold')
	one = matchObj.group('one')
	two = matchObj.group('two')
	return one+'<span class="bold">'+s+'</span>'+two

def replItalics(matchObj):
	s = matchObj.group('italics')
	three = matchObj.group('three')
	four = matchObj.group('four')
	return three+'<span class="italics">'+s+'</span>'+four


count = 0
i = 0
l = 0

for line in file:
	line = regex.sub('',line)
	line = bold.sub(replBold,line)
	line = italics.sub(replItalics,line)
	file_o.write(line)
	count += 1
	i += 1
	if i > 1000:
		print(count,end='\r')
		i = 0
print("lines written = {} out of {}".format(count,count))