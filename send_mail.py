SERVER = "smtp-mail.outlook.com"
FROM = "tsq-ttp@outlook.com"
PASSWORD = "TSQ1234@"
TO = ["yudha.gunslinger@gmail.com"] # must be a list


SUBJECT = "Hello!"
TEXT = "This is a test of emailing through smtp in outlook."

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, message)
server.quit()