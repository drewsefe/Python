import smtplib
import ssl

#setup port number and server name
smtp_port = 587
smtp_server = 'smtp.gmail.com'

email_from = 'drewsefe2@gmail.com'
email_to = 'drewsefe2@gmail.com'

pswd = 'adftyonjylhchnbd'

#content of message
message = 'This is a test to determine whether the automation is running smoothly'
simple_email_context = ssl.create_default_context()


try: 
    print('Connecting to server....')
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd )
    print("Connected to Server")
    
    print()
    print(f'Sending email to - {email_to}')
    TIE_server.sendmail(email_from, email_to, message)
    print(f'Email successfully sent to - {email_to}')
    
except Exception as e:
    print(e)
    
finally: 
    TIE_server.quit()
    