import os

pathName = os.path.abspath("requesthtml.exe") # finds the path of the proper file
# in my case it should return C:\\Users\\90499\\dist\\requesthtml.exe
commandTask = "schtasks /Create /SC MINUTE /TN requesthtml /TR " + pathName
os.system(commandTask) 
