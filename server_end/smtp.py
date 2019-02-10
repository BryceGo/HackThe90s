import smtplib

server_name = "smtp.gmail.com"
server_port = 587

client_email = "vleon@sfu.ca"
client_password = ""


def send(email_subject, email_body): #Sends the message
    try:
        conn = smtplib.SMTP(server_name,server_port)
        conn.ehlo()
        conn.starttls()
        conn.login(client_email, client_password)
        conn.sendmail(client_email, client_password, 'Subject:' + email_subject + '\n\n' + email_body)
        conn.quit()
        print('Success')
    except smtplib.SMTPServerDisconnected:
        print('Server disconnected unexpectedly')
    except smtplib.SMTPSenderRefused:
        print('Sender address invalid')
    except smtplib.SMTPRecipientsRefused:
        print('All recipient addresses have been refused')
    except smtplib.SMTPDataError:
        print('SMTP Server does not accept the message data')
    except smtplib.SMTPConnectError:
        print('Could not establish a connection with the server')
    except smtplib.SMTPHeloError:
        print('Server refuses the HELO message')
    except smtplib.SMTPAuthenticationError:
        print('Authentication Error, Incorrect username or password')
        print('Try allowing unsecure logins to your account')
    except:
        print('Unknown Error')
