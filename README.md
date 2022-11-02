# Data Projects
Miscellaneous data and software projects that I'm currently working on at Napleton Automotive.

# Project Descriptions
## pull_data.py
Relatively simply python program to connect to custom built Node.js API and pull data using requests. The goal was to gain proficiency in collecting and normalizing data in order to prepare it for visualization with Matplotlib or other graphing libraries. Another goal in this project was to get better at optimizing functions and error handling. 

##email_verify.py
This project was rather interesting as our organization was moving to a new email system and thus required all users to have a working email and password on file. This was unforuntely not the case and it meant that we had to manually check over 4000 emails against a login portal via copy paste of credentials. I informed my Systems Admin that I can automate this entire process and wrote this script in a few hours. It takes a list of users with emails and passwords in a JSON file and recursively navigates each JSON value and key to verify the email/password combo against our email server. This utilizes the **smtplib** python library. 



