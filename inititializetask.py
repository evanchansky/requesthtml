import os

os.system("pipenv run pyinstaller --onefile --noconsole -y requesthtml.py")		

exePathName = "C:\\Users\\90499\\ServerCheck\\requesthtml.exe" 									# Finds path the newly created .exe file
commandSchtask = "schtasks /Create /SC MINUTE /TN requesthtml /TR " + exePathName 			# Builds cmd line for creating the repeated task
print(commandSchtask)
os.system(commandSchtask) 																	# Creates the task
