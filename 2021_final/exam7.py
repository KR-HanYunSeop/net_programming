import paramiko
import getpass
import time
import smtplib
from email.message import EmailMessage
import filetype


filename = '20201690.zip' # 압축파일의 이름
dirname = '/home/net_pro/20201690' # 압축할 폴더
CMD = 'zip -r ' + filename + ' ' + dirname + '\n' # 리눅스 압축 명령어

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

# stdin, stdout, stderr = ssh.exec_command('mkdir 20191535')
# stdin, stdout, stderr = ssh.exec_command('echo iot > iot.txt')
# stdin, stdout, stderr = ssh.exec_command(CMD)

channel = ssh.invoke_shell() # 새로운 셸 세션(channel) 생성

# 채널을 통해 명령어 전송
channel.send('mkdir 20201690\n')
time.sleep(0.5)
channel.send('cd 20201690\n')
time.sleep(0.5)
channel.send('echo iot > iot.txt\n')
time.sleep(0.5)
channel.send('cd ..\n')
time.sleep(0.5)
channel.send(CMD)
time.sleep(0.5)

sftp = ssh.open_sftp()

sftp.get(filename, filename)

sftp.close()
ssh.close()


# 보내는 메일 서버
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
# 순천향 대학교 465
# gmail 587

# 송신자, 수신자, 비밀번호
sender = 'bulgu1202@gmail.com'
recipient = 'nocut1202@naver.com'
password = 'qbzgwedpdssmhirb'

# 메시지 생성하기
msg = EmailMessage()
msg['Subject'] = '20201690.zip'
msg['From'] = sender
msg['To'] = recipient
text = '20201690 한윤섭'
msg.set_content(text)
with open('20201690.zip', 'rb') as f:
    data = f.read()

# add_attachment 함수를 이용해 파일 첨부. 파일 첨부시 첨부된 파일의 mime-type 지정
msg.add_attachment(data, maintype='image', subtype=filetype.guess_mime(data), filename='20201690.zip')


# SMTP 객체 생성 후, 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()        #stmp서버로 hello메시지 전송
s.starttls()    #tls 실행
s.login(sender, password)   #로그인
s.send_message(msg)         #메시지 전송
s.quit()