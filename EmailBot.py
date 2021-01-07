import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender_mail@gmail.com', 'password')
server.sendmail('sender_mail@gmail.com',
                'receiver_mail@gmail.com',
                'type message here which you want to send'
                )