#!/usr/bin/env python3
import sys
from subprocess import call
import os

if len(sys.argv) == 2:
	ffrom = 1
	fto = 73
	delprev = 'y'
	orig = sys.argv[1]

elif len(sys.argv) == 5:
	ffrom = int(sys.argv[1])
	fto = int(sys.argv[2])
	delprev = sys.argv[3]
	orig = sys.argv[4]

else:
	print("Wrong number of arguments")
	help()


if delprev not in ['y','n']:
	print('wrong third argument')
	exit()

file = "scripts/N"+str(ffrom-1)+".xml"
if os.path.exists(file):
	os.remove(file)
	
os.symlink(os.getcwd() + "/" + orig, file)

os.chdir("./scripts")

for i in range(ffrom,fto+1):
	d = "N"+str(i-2)+".xml"
	if delprev == 'y' and os.path.exists(d):
		os.remove(d)
	file = "N"+str(i)+".py"
	print(file)
	if not os.path.exists(file):
		print(file+" doesn't exist!")
		exit()
	call(["python3",file])

def help():
	print("./runScripts.py <dump_file_to_parse>")
	print("./runScripts.py <from> <to> <delete_previous_generated_file> <file_to_start_parsing_from>")
	print("		from: 1-75, script to run from. There must be pre-processed file corresponding to stating script")
	print("		to: 1-75, script to run upto")
	print("		delete_previous_generated_file: y or n, delete previous generated file to save space")
	exit()