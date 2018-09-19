import re
import os

inputfile1 = open('i.txt')
inputfile2 = open('am.txt')
inputfile3 = open('myName.txt')
if not os.path.exists('bin'):
	os.mkdir('bin')
outputfile = open('bin\output.txt', 'w+')

for line in inputfile1:
	outputfile.write(line)
for line in inputfile2:
	outputfile.write(line)
for line in inputfile3:
	outputfile.write(line)

inputfile1.close
inputfile2.close
inputfile3.close
outputfile.close