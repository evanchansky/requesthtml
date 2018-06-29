import os

os.system("schtasks /Create /SC MINUTE /TN requesthtml TR/ C:\\Users\\90499\\dist\\requesthtml.exe") 
# the path off the executable file will have to be changed for where the file is saved
