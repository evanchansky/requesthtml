import os

os.system("pip install requests")
os.system("pip install pyinstaller")

pathName = os.path.abspath(os.path.dirname(__file__))
specPathName = os.path.join(pathName, "requesthtml.spec")
exePathName = os.path.join(pathName, "requesthtml.exe")
pathFileName = os.path.join(pathName, "path.txt")

f = open(pathFileName, "w") 
f.write(pathName) 				# writes path of folder to a fuile that can be used by other scripts
f.close()

cmdPacakageExe = "pyinstaller -F --distpath=%s %s"	% (pathName, specPathName)
print(cmdPacakageExe)
os.system(cmdPacakageExe)

commandSchtask = "schtasks /Create /SC MINUTE /MO 5 /TN requesthtml /TR %s" % (exePathName)		# Builds cmd line for creating the repeated task
print(commandSchtask)
os.system(commandSchtask) 	# Creates the task

wait = input("All set! Press enter to continue: ")				
