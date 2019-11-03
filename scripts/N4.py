
import os

f = os.path.basename(__file__).split('.')[0]
outseq = int(f[1:])
inseq = outseq - 1

file = open("N"+str(inseq)+".xml","r",buffering=1,encoding='utf-8')
file_o = open("N"+str(outseq)+".xml","w",buffering=1,encoding='utf-8')

# may include etymology
#proper noun missing like Georgia

markers = ['adjective', 'adverb', 'ambiposition', 'article', 'circumposition', 'classifier', 'conjunction', 'counter', 
			'determiner', 'ideophone', 'interjection', 'noun', 'numeral', 'participle', 'particle', 'postposition', 'preposition', 
			'pronoun', 'proper noun', 'verb','antonym', 'synonym', 'meaning', 'contraction', 'alternative form', 'phrase','proverb', 'prepositional phrase','pronunciation']

select = False
count = 0
total = 0
l = 0

for line in file:
	total += 1
	l += 1
	if l > 1000:
		l = 0
		print(count,end='\r')
	if line.startswith('<title>'):
		select = True
	elif line.startswith('='):
		select = False
		candidates = line.split('=')
		candidates_lstripped = [ c.lstrip().lower() for c in candidates ]
		for item in candidates_lstripped:
			if item == '':
				continue
			for marker in markers:
				if item.startswith(marker):
					select = True
					break
			if select:
				break
	if select:
		file_o.write(line)
		count += 1

print("{} lines pruned out of {}".format(count,total))

