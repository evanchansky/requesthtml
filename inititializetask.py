import os

# Finds path and directory of this file to direct and then locate the exe file
pathName = os.path.abspath(os.path.dirname(__file__))	
specPathName = os.path.join(pathName, "requesthtml.spec")
exePathName = os.path.join(pathName, "requesthtml.exe")
pathFileName = os.path.join(pathName, "path.txt")

f = open(pathFileName, "w") 
f.write(pathName)
f.close()

commandPackageExe = """pipenv run pyinstaller --onefile --noconsole -y --distpath="%s" "%s\\requesthtml.py" """ % (pathName,specPathName)
print(commandPackageExe)
os.system(commandPackageExe)					# Packages python script into executable with necessary dependencies

commandSchtask = """schtasks /Create /SC MINUTE /TN requesthtml /TR "%s\\requesthtml.exe" """	% (exePathName)		# Builds cmd line for creating the repeated task
print(commandSchtask)
os.system(commandSchtask) 

wait = input("All set! Press enter to continue: ")
