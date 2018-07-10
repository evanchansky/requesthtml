import requests
import json
import datetime
import sys
import configparser

def format_timestamp():
	dt = datetime.datetime.now()
	timestamp = dt.strftime("%d/%m/%Y %H:%M:%S")
	return timestamp

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
	log = open("C:\\Users\\90499\\ServerCheck\\serverLog.txt", 'a')
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
	config = configparser.ConfigParser()
	config.read('C:\\Users\\90499\\ServerCheck\\requesthtml_Config.ini')

	SENDER = config['Setup']['UserEmail']			# email address the message will be sent from (must be gmail account to use gmail server)
	PASSWORD = config['Setup']['UserPassword']		# password to the SENDER account
	RECEIVER = config['Setup']['AdminEmail']		# email address that the alert will be sent to (does not have to be a gmail account)	
	URLs = config['Setup']['ServerURLs'].split('\n')
	for SERVERLINK in URLs:
		check_URL(SENDER, PASSWORD, RECEIVER, SERVERLINK)

main()
