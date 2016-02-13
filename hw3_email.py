# coding=utf-8
import smtplib
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-email_sen')
parser.add_argument('-email_rec')
parser.add_argument('-email_psw')
parser.add_argument('-host')
parser.add_argument('-port')
parser.add_argument('-subject')
parser.add_argument('-email_body', nargs='*')

args = parser.parse_args()

print(args.subject)
print(args.email_sen)
print(args.email_rec)
print(args.email_body)
print(args.host)
print(args.port)

from email.message import Message

from email.header import Header

msg = Message()

#msg.set_charset("utf-8")

#h = Header(args.email_sen.encode('utf-8'), 'utf-8')

msg["Subject"] = args.subject

text = args.email_body

#msg.set_payload(text.encode('utf-8'))
s_emailbody = ' '.join(args.email_body)
print(s_emailbody)
msg.set_payload(s_emailbody)
smtp_obj = smtplib.SMTP(args.host, args.port) #'smtp.yandex.ru', 587
smtp_obj.starttls()
smtp_obj.login(args.email_sen, args.email_psw)
smtp_obj.sendmail(args.email_sen, args.email_rec, msg.as_string())
smtp_obj.quit()