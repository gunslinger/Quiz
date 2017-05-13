def send_mail(recipient, subject, message):

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    username = "tsq-ttp@outlook.com"
    password = "TSQ1234@"
    EMAIL_PORT = 587  # Port 587 is reserved for TLS
    EMAIL_USE_TLS = False  # But you have disabled TLS

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('sending mail to ' + recipient + ' on ' + subject)

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 25)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

    except error as e:
        print(str(e))


send_mail('yudha.gunslinger@gmail.com', 'Sent using Python %s' % 'yuda', 'May the \nforce be \nwith you. %s' % 'yuda')