import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'bulgu1202@gmail.com'
recipient = '20201690@sch.ac.kr'
password = 'qbzgwedpdssmhirb'

msg = EmailMessage()
msg['Subject'] = '이메일 테스트'
msg['From'] = sender
msg['To'] = recipient
text = '네트워크 프로그래밍 e-mail test'
msg.set_content(text)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()