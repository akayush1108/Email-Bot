import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender_mail@gmai,com', 'password')
server.sendmail('sender_mail@gmail.com',
                'receiver_mail@gmail.com',
                'message which you want to send'
                )