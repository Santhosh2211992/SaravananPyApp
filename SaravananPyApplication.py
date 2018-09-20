import os
import subprocess
import shutil
import sys
from subprocess import Popen, PIPE

currentWorkingDir = os.getcwd()
repoPath = currentWorkingDir + "\SaravananPyApp"

#Getting Version of Git and Python

gitVersion = os.popen("git --version").read()
print('git --version: ' + str(gitVersion))

pythonVersion = sys.version
print('Python Version: ' + str(pythonVersion))
#sys.exit()

lastCommitID = ""
currentCommitID = ""

if not os.path.exists(repoPath):
    os.system("git clone https://Santhosh2211992:TestGit22@github.com/Santhosh2211992/SaravananPyApp.git")
    os.chdir(repoPath)
    cmd = "git rev-parse HEAD"
    lastCommitID = os.popen(cmd).read()
    currentCommitID = lastCommitID
    #print("lastCommitID: ", lastCommitID)
    #print("currentCommitID: ", currentCommitID)
else:
    os.chdir(repoPath)
    cmd = "git rev-parse HEAD"
    lastCommitID = os.popen(cmd).read()
    os.system("git pull")
    cmd = "git rev-parse HEAD"
    currentCommitID = os.popen(cmd).read()
    #print("lastCommitID: ", lastCommitID)
    #print("currentCommitID: ", currentCommitID)

#checking if lastcommitID and currentCommitID are matching

if (lastCommitID == currentCommitID):
	print("No new commits, skipping the build")
else:
	print("New changes are available, Building...")
	source = os.path.join(repoPath, 'build' + '.' + 'bat')
	#####source = repoPath + "\" + "build.bat"
	#print("source: " + source)
	#####destination = currentWorkingDir + "\build.bat"
	destination = currentWorkingDir
	shutil.copy(source, destination)
	os.chdir(currentWorkingDir)
	cmdlinePassing = "build.bat" + " " + "SaravananPyApp"
	#print("cmdlinePassing:  " + cmdlinePassing)
	#os.system(cmdlinePassing) # need to do error handling here
	p = Popen(['build.bat', 'SaravananPyApp'], stdout=PIPE, stderr=PIPE)
	output, error = p.communicate()
	output=output.decode("utf-8")
	error=error.decode("utf-8")

	if p.returncode != 0:   ## error case
		print("output : " + str(output))
		print ("********************")
		print("Error : " + str(error))
		## call email function
		## fetch all changes happend
		## attach logs of output and error
	else:
		# add/update contents of bin folder
		os.chdir(repoPath)
		# # Git push the built changes  to remote
		os.system("git add .")
		os.system("git commit -m \"Build successfully completed for changes\"")
		os.system("git push origin")
	
## Email function	

	












