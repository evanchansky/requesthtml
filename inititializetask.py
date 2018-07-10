import os

exePathName = "C:\\Users\\90499\\ServerCheck" 	# Finds path the newly created .exe file - NEEDS TO BE ABLE TO FIND THIS AUTOMATICALLY

commandPackageExe = "pipenv run pyinstaller --onefile --noconsole -y --distpath=%s %s\\requesthtml.py" % (exePathName,exePathName)
print(commandPackageExe)
os.system(commandPackageExe)
																					# Packages python script into executable with necessary dependencies
commandSchtask = "schtasks /Create /SC MINUTE /TN requesthtml /TR %s\\requesthtml.exe"	% (exePathName)		# Builds cmd line for creating the repeated task
print(commandSchtask)
os.system(commandSchtask) 

wait = input("Press enter to continue")	
