'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'surenkumar13579@gmail.com'
email_passwd = 'iwwp hrsn kscr jove'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='surendesaboina@gmail.com', msg="Sent from my IDE. Hehe")
connection.close()
print('Mail sent successfully')