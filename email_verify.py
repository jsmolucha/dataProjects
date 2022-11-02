import smtplib
import json

f = open(_ENV.dataFile)
data = json.load(f)

good_emails = []
bad_emails = []
missing_pword = []

for i in range(len(data['users'])):
    try:
        username = data['users'][i]['username']
        password = data['users'][i]['Password']
        
        print("Checking: ",username," with password: ",password)

        if password == '':
            missing_pword.append(username)

        #testing to find length of list//////
        f.close()

        server = smtplib.SMTP_SSL(_ENV.emailServer, _ENV.serverPort)

        server.set_debuglevel(0)    

        # add them here////////////////////////////////
        user = server.login(username, password)

        # and add them here ///////////////////
        server.mail(username)

        code, message = server.rcpt(_ENV.recipient)
        
        # sanity check the authentication status of the email 
        if code == 250:
            print("Email Authenticated, Status:  ", code)
            print('\n')
        else:
            print("Bad")

        server.quit()

    except:
        # negating that stupid exception error from 500 level error 
        # and just adding the entry to a list stored in memory
        bad_emails.append(username)
        print("Bad Password on email: ", username)
        print('\n')

# finalized result, print all bad and empty emails in a list
print("Bad emails: ")
print(bad_emails)
print('\n')
print("Emails missing password: " )
print(missing_pword)


