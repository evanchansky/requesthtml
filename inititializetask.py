import os
pathName = os.path.abspath("requesthtml.exe") # in this case it should return C:\\Users\\90499\\dist\\requesthtml.exe
print(pathName)
commandTask = "schtasks /Create /SC MINUTE /TN requesthtml /TR " + pathName
os.system(commandTask) 
# the path off the executable file will have to be changed for where the file is saved
