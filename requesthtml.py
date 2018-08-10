import requests				# For pinging the URL for info
import json					# For parsing the JSON object the URL provides
import datetime				# For timestamping the log
import sys
import os	
import smtplib				# for sending emails
import configparser			# For parsing the config file

FirstResourceCall = True

# Description: Formats the current date and time and returns it as a string		
# Arguments: none
# Returns: The current date and time in a formatted string
# Modules called: none
def format_timestamp():
	dt = datetime.datetime.now()
	timestamp = dt.strftime("%d/%m/%Y %H:%M:%S")
	return timestamp

# Description: Finds the proper path and combines it with the extension given
# Arguments: fileName - name of file and type (i.e. serverLog.txt)
# Returns:  filePath - the complete path to a file (i.e C:\Users\90499\ServerCheck\serverLog.txt)
# Modules called: none
def resource_path(fileName):		
	global FirstResourceCall
	if FirstResourceCall:							
		FirstResourceCall = False
	
	# Get absolute path to resource, works for dev and for PyInstaller 
	if hasattr(sys, '_MEIPASS'):										# The temp folder created when pyinstaller runs a bundled exe
		if FirstResourceCall:							# Makes sure to only change the directory on the first call
			os.chdir(sys._MEIPASS)							
		filePath = os.path.join(sys._MEIPASS, fileName)
	else:
		filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), fileName)

	return filePath

# Description: Parses the JSON from the URL and logs the info
# Arguments: str - JSON object in string form from URL; statusLog - file where server version from JSON str is logged 
# Returns: none but appends a new entry to the file
# Modules called: format_timestamp
def json_parse(str, statusLog):
	print("Parsing the json...")
	result = json.loads(str)
	try:
		var = result['data']['version']
		print('The server is working well') 
		newEntry = format_timestamp() + '\t ' + var + '\n'
		statusLog.write(newEntry)
		print('The current app server version is',var)
	except ValueError:
		print('We can not parse the string.')
  
# Description: Sends and email according to specifications and logs result
# Arguments: user - email adress the email is sent FROM
#			 pwd - password to user email address
#			 recipient - email addres the temail is sent TO
# 			 log - serverLog file to log the email status
# Returns: nothing but adds email status to log to show there was an error with the server 
#		   and whether or not an email was sent
# Modules called:   format_timestamp
def send_email(user, pwd, recipient, log):

	FROM = user
	TO = recipient if isinstance(recipient, list) else [recipient]
	SUBJECT = 'Server Error'
	TEXT = 'The mobile server might be down, please check'

	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)	# server and port
		server.ehlo()									# Identifies self to server
		server.starttls()								# Starts TLS encryption 
		server.login(user, pwd)							# Logs in to the server
		server.sendmail(FROM, TO, message)				# Actually send the message
		server.close()									# Closes connection to server
		print ('successfully sent the mail')
		newEntry = format_timestamp() + '\t ERROR: EMAIL SENT\n'
		statusLog.write(newEntry)
	except:
		print ("failed to send mail")
		newEntry = format_timestamp() + '\t ERROR: EMAIL NOT SENT\n'
		statusLog.write(newEntry)

# Description:  Requests server info from URL and calls JSON parse module to get server version
#				Calls the send email module if URL times out
# Arguments: 	user - email adress the email is sent FROM
#			 	pwd - password to user email address
#			 	recipient - email addres the temail is sent TO
#				link - the URL that will be checked
# 			 	log - serverLog file to log the email status
# Returns: Nothing, but the jsonParse and check_URL
# Modules called: json_parse, send_email
def check_URL(user, pwd, recipient, link, log):
	try:	
		response = requests.get(link, timeout=10) 				#TO TEST EMAIL: change timeout to .00001 
		json_parse(response.text, log)
	except requests.exceptions.RequestException as e:
		print('The server doesn''t answer...')
		print('Sending Email to administrator...')
		send_email(user, pwd, recipient, log)
		print(e)
	

# Description:	Main module that sets everything up and runs other modules
#				Reads values from config file and runs check_URL for all URLs
# Arguments:	none
# Returns: 		none
# Modules called: 	resource_path, check_URL
def main():
	
	
	folderPathFile = resource_path("path.txt")
	with open(folderPathFile) as f:
		folderPathName = f.read()
	print(folderPathName)
	
	logFile_Name = os.path.join(folderPathName, "serverLog.txt") 			
	SERVERLOG = open(logFile_Name, 'a')
	
	config = configparser.ConfigParser()
	configFile_Name = resource_path("requesthtml_Config.ini")					
	config.read(configFile_Name)
	SENDER = config['Setup']['UserEmail']			# email address the message will be sent from (must be gmail account to use gmail server)
	PASSWORD = config['Setup']['UserPassword']		# password to the SENDER account
	RECEIVER = config['Setup']['AdminEmail']		# email address that the alert will be sent to (does not have to be a gmail account)	
	URLs = config['Setup']['ServerURLs'].split('\n')
	for SERVERLINK in URLs:
		check_URL(SENDER, PASSWORD, RECEIVER, SERVERLINK, SERVERLOG)
	SERVERLOG.close()
	print("you are at the end")

main()
