import re
import os
import sys
import datetime

OUTPUT = "output_" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"

print("[INFO] : Builder.py started executing")

cwd = os.getcwd()
repoPath = sys.argv[1]
os.chdir(repoPath)

inputfile1 = open('i.txt')
inputfile2 = open('am.txt')
inputfile3 = open('myName.txt')
if not os.path.exists('bin'):
	os.mkdir('bin')
outputfile = open('bin' + '\\' + OUTPUT, 'w+')

for line in inputfile1:
    print("[INFO] : Processing data from file i.txt")
	outputfile.write(line)
for line in inputfile2:
    print("[INFO] : Processing data from file am.txt")
	outputfile.write(line)
for line in inputfile3:
    print("[INFO] : Processing data from file myName.txt")
	print("[INFO] : Preparing the file " + OUTPUT)
	outputfile.write(line)

	
inputfile1.close
inputfile2.close
inputfile3.close
outputfile.close

os.chdir(cwd)

print("**********************************************************")
print("build.bat completed successfully")
print("**********************************************************")