# requesthtml
### Code to automatically check server and send email to administrator if it is down
1. Enter login information into the config file requesthtml_Config.ini
   - UserEmail = the email address the alert email will be sent from: **_MUST_ be a _GMAIL_ account to use the Gmail SMTP**
   - UserPassword = the password to the above email address
   - AdminEmail = the administrator email address that will recevie an alert if the server is down (can be **ANY** email address)
   - ServerURL = the URL or list of URLs to be checked: **seperate URLs by _NEW LINES_** 
   - Here's what it should look like:
   
 [Setup]
 UserEmail = you@gmail.com <br />
 UserPassword = password <br />
 AdminEmail = admin@example.com <br />
 URLS = https://some_server_link.com <br />
   https://and_here_is_another_one.com <br />
   
   
2. Run the script "InitializeTask.py" by doubkle clicking it
3. You are all set from here! Here is what the code does:
   - The code packages the script requesthtml.py into an .exe file with the proper configuration values (all in the same folder)
   - The code runs a cmd to start a schtasks task that runs requesthtml.exe every 5 minutes
4. To delete the task, run the cript "deleteTask.py"
