# requesthtml
### Code to automatically check server and send email to administrator if it is down
1. Enter login information into the config file requesthtml_Config.ini
   - UserEmail = the email address the alert email will be sent from: **MUST** BE A **GMAIL** ACCOUNT TO USE GMAIL SMTP
   - UserPassword = the password to the above email address
   - AdminEmail = the administrator email address that will recevie an alert if the serve is down (can be **ANY** email address)
   - ServerURL = the URL or list of URLs to be checked: SEPERATE URLS BY **NEW LINES** 
2. Run the command "python InitializeTask.py" in Windows command script
3. The code packages the script requesthtml.py into an .exe file with the proper configuration values (all in the same folder)
4. The code runs a cmd to start a schtasks task that runs requesthtml.exe every 5 minutes
5. To delete the task, type "schtasks /delete /tn requesthtml"
