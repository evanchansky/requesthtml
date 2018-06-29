import requests
import json
import time

def jsonParse(str):
    print("Parsing the json...")
    result = json.loads(str)
    try:
        var = result['data']['version']
        print('The server is working well')        
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
        server.sendmail(FROM, TO, message)				# Actually send ths message
        server.close()									# Closes connection to server
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")



def check_URL(user, pwd, recipient, link):
	try:
		response = requests.get(link, timeout=10)
		jsonParse(response.text)
	except requests.exceptions.RequestException as e:
		print('The server doesn''t answer...')
		print('Sending Email to administrator...')
		send_email(SENDER, PASSWORD, RECEIVER,'Server Error','The mobile server might be down, please check')
		print(e)

#Enter your information here in quotes

SENDER = 'evanchansky@gmail.com'						# email address the message will be sent from (must be gmail account to use gmail server)
PASSWORD = 'emanrules'									# password to the SENDER account
RECEIVER = 'Chansky.EvanDouglas@hutchisonports.com'		# email address that the alert will be sent to (does not have to be a gmail account)	
URL = 'https://mobileapps-as.hutchisonports.com/resources_hpt/server/status'
check_URL(SENDER, PASSWORD, RECEIVER, URL)
