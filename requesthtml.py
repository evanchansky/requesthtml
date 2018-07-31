import requests
import json
import datetime
import sys
import os
import configparser

def format_timestamp():
	dt = datetime.datetime.now()
	timestamp = dt.strftime("%d/%m/%Y %H:%M:%S")
	return timestamp

def resource_path(fileName):		
	# Get absolute path to resource, works for dev and for PyInstaller 
	wait = input("this module has been called")
	if hasattr(sys, '_MEIPASS'):
		os.chdir(sys._MEIPASS)
		filePath = os.path.join(sys._MEIPASS, fileName)
	else:
		filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), fileName)
		
	check = input(filePath)
	return filePath

def jsonParse(str, statusLog):
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
    
def send_email(user, pwd, recipient, subject, body):
	import smtplib

	FROM = user
	TO = recipient if isinstance(recipient, list) else [recipient]
	SUBJECT = subject
	TEXT = body

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
	except:
		print ("failed to send mail")

def check_URL(user, pwd, recipient, link):
	log = open("serverLog.txt", 'a')
	try:	
		response = requests.get(link, timeout=10)
		jsonParse(response.text, log)
	except requests.exceptions.RequestException as e:
		print('The server doesn''t answer...')
		print('Sending Email to administrator...')
		newEntry = format_timestamp() + "\t ERROR: EMAIL SENT \n" 
		log.write(newEntry)
		send_email(user, pwd, recipient,'Server Error','The mobile server might be down, please check')
		print(e)
	log.close()

def main():
	pathFile = resource_path("path.txt")
	with open(pathFile) as f:
		pathName = f.read()
	print(pathName)
	
	logFile_Name = 	os.path.join(pathName, "serverLog.txt")		
	SERVERLOG = open(logFile_Name, 'a')
	
	config = configparser.ConfigParser()
	configFile_Name = resource_path("requesthtml_Config.ini")
	config.read('requesthtml_Config.ini')

	SENDER = config['Setup']['UserEmail']			# email address the message will be sent from (must be gmail account to use gmail server)
	PASSWORD = config['Setup']['UserPassword']		# password to the SENDER account
	RECEIVER = config['Setup']['AdminEmail']		# email address that the alert will be sent to (does not have to be a gmail account)	
	URLs = config['Setup']['ServerURLs'].split('\n')
	for SERVERLINK in URLs:
		check_URL(SENDER, PASSWORD, RECEIVER, SERVERLINK, SERVERLOG)

main()
