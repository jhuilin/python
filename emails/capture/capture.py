import cv2
import smtplib
from email.mime.text import MIMEText

def getPic(self):
    cap = cv2.VideoCapture(0)                   # open camera
    ret, frame = cap.read()                     # get picture
    cv2.imwrite(self.path + 'pic.jpg', frame)   # save the picture path
    cap.release()                               # turn of camera

def setMassge(self):
    msg = MIMEMultipart('mixed')
    msg['Subject'] = 'The Mac is opened'
    msg['From'] = 'jianhuilin@yahoo.com'
    msg['to'] = sefl.receive

    text = 'Your mac is opened, and capture below image:'

    text = MIMEtext(text, 'plain', 'utf-8')
    msg.attach(text)
    send_img = open(self.path + 'pic.jpg', 'rb').read()
    img = MIMEImage(send_img)
    img['Content-Disposition'] = 'attachment; filename = "login.png"'
    msg.attach(img)
    return msg.as_string()

def __init__(self):
    self.smtpserver = 'smtp.mail.yahoo.com'
    self.user = 'jianhuilin@yahoo.com'
    self.pw = 'mogljludwdnfojmg'
    self.sender = 'jianhuilin@yahoo.com'
    self.receive = 'jianhuilin1124@gmail.com'
    self.max_num = 5
    self.path = './images/'

def sendEmail(self,msg):
    smtp = smtplib.SMTP()
    smtp.connect('smtp.yahoo.com')
    smtp.login(self.user, self.pw)
    smtp.sendmail(self.sender,self.receive,msg)
    smtp.quit()
