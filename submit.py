import tkinter as tk
from tkinter import *
import tkinter.font as font
import smtplib
import email
from email.header import decode_header
from imapclient import IMAPClient
import imaplib

sender_host = 'smtp.gmail.com'
reciever_host = 'imap.gmail.com'


def compose_new():
	window = tk.Tk()
	window.title('Compose')
	greeting = tk.Label(text="Create new mail", foreground='Green', background='Black', width=60)
	myfont = font.Font(family='Helvetica')
	label5 = tk.Label(text="To")
	label6 = tk.Label(text="Subject")
	label7 = tk.Label(text="Body")
	reciever_id = tk.Entry(bg='pink', fg='green')
	entrysub = tk.Entry(bg='black', fg='green', width=50)
	entrymain = tk.Text(bg='black', fg='green', width=50, height=10)
	greeting['font'] = myfont
	reciever_id['font'] = myfont
	entrysub['font'] = myfont
	entrymain['font'] = myfont
	def d(reciever_id,entrymain):
		global reciever
		reciever=reciever_id.get()
		global msg1
		msg1=entrymain.get("1.0",'end-1c')
	sendmail = tk.Button(text="Send", foreground='Yellow', background='Red', command=lambda:[d(reciever_id,entrymain),compose2()])
	sendmail['font'] = myfont
	greeting.pack()
	label5.pack()
	reciever_id.pack()
	label6.pack()
	entrysub.pack()
	label7.pack()
	entrymain.pack()
	sendmail.pack()
	window.mainloop()


def main_page():
	print("Welcome buddy!!!")
	root = tk.Tk()
	root.title('Homepage')

	def b():
		root.destroy()
	greeting = tk.Label(text="Welcome to Homepage", foreground='Green', background='Black', width=60, height=2)
	greeting.pack()
	topFrame = Frame(root)
	topFrame.pack()
	myfont = font.Font(family='Helvetica')
	create = tk.Button(topFrame, text='Compose', bg='Red', fg='green', width=30, command=lambda:[b(),compose_new()])
	inbox = tk.Button(topFrame, text='Inbox', bg='Red', fg='green', width=30, command=read_inbox)
	sent = tk.Button(topFrame, text='Sent', bg='Red', fg='green', width=30, command=read_sent)
	delete_all_read = tk.Button(topFrame, text='Delete all unseen', bg='Red', fg='green', width=30, command=delete_unseen)
	delete_all = tk.Button(topFrame, text='Delete all', bg='Red', fg='green', width=30, command=delete_all_inbox)
	logout = tk.Button(text="Logout", foreground='Yellow', background='Red', command=logout_account)
	create['font'] = myfont
	inbox['font'] = myfont
	sent['font'] = myfont
	delete_all['font'] = myfont
	delete_all_read['font'] = myfont
	logout['font'] = myfont
	create.pack()
	inbox.pack()
	sent.pack()
	delete_all.pack()
	delete_all_read.pack()
	logout.pack()
	root.mainloop()


##login page
'''
def login1():
	window1 = tk.Tk()
	window1.title('Login')
	def a():
		window1.destroy()
	myfont = font.Font(family='Helvetica')
	greeting = tk.Label(text="Login to your Account.", foreground='Green', background='Black', width=60, height=2)
	label1 = tk.Label(text="Email-Id")
	label2 = tk.Label(text="Password")
	user1 = tk.Entry(text='Username', bg='Black', fg='Green')
	user1['font'] = myfont
	password1 = tk.Entry(text='Password', bg='black', fg='Green')
	password1['font'] = myfont
	global user
	user=user1.get()
	global password
	password=password1.get()
	button = tk.Button(text="Login", foreground='Yellow', background='Red',command=lambda:[a(),main_page()])
	button['font'] = myfont

	greeting.pack()
	label1.pack()
	user1.pack()
	label2.pack()
	password1.pack()
	button.pack()
	window1.mainloop()
'''
def compose2():
	try:
		session = smtplib.SMTP(sender_host, 587)
		session.starttls()
		session.login(user, password)
		session.sendmail(user, reciever, msg1)
		print("Email sent successfully")
		session.quit()
	except:
		print("Error!!!,Unable to send email..")


def read_inbox():
	try:
		session2 = imaplib.IMAP4_SSL(reciever_host)
		session2.login(user, password)
		status, message = session2.select('Inbox')
		N = 5
		message = int(message[0])
		for i in range(message, message - N, -1):
			res, msg2 = session2.fetch(str(i), "(RFC822)")
			for response in msg2:
				if isinstance(response, tuple):
					msg2 = email.message_from_bytes(response[1])
					subject = decode_header(msg2["Subject"])[0][0]
					if isinstance(subject, bytes):
						subject = subject.decode()
					from_ = msg2.get("From")
					print("Subject:", subject)
					print("From:", from_)
	except:
		print("SORRY :( ,Could not read inbox")


def logout_account():
	try:
		session2 = imaplib.IMAP4_SSL(reciever_host)
		session2.login(user, password)
		print(session2.logout()[0])
		print("You have successfully logged out.")
	except:
		print('SORRY!!!  Try again.')


def delete_unseen():
	try:
		session = IMAPClient(reciever_host, ssl=True, port=993)
		session.login(user, password)
		session.select_folder('Inbox')
		delmail = session.search('UNSEEN')
		session.delete_messages(delmail)
		print("You have successully deleted all unread mails.")
	except:
		print("Sorry!!! Try again.")

def delete_all_inbox():
	try:
		session = IMAPClient(reciever_host, ssl=True, port=993)
		session.login(user, password)
		session.select_folder('Inbox')
		delmail = session.search('ALL')
		session.delete_messages(delmail)
		print("You have successully deleted all of your mails in Inbox.")
	except:
		print("Sorry!!! Try again")


def read_sent():
	try:
		session2 = imaplib.IMAP4_SSL(reciever_host)
		session2.login(user, password)
		status, message = session2.select('"[Gmail]/Sent Mail"')
		N = 5
		message = int(message[0])
		for i in range(message, message - N, -1):
			res, msg2 = session2.fetch(str(i), "(RFC822)")
			for response in msg2:
				if isinstance(response, tuple):
					msg2 = email.message_from_bytes(response[1])
					From = msg2["From"]
					subject = msg2["Subject"]
					To = msg2["To"]
					Bcc = msg2["Bcc"]
					Body = msg2["Body"]
					#print("From :", From)
					print("Subject :", subject)
					print("Bcc :", Bcc)
					print("To :", To)
					#print("Body :", Body)

	except:
		print("Sorry!!!,Try again")


#login1()

window1 = tk.Tk()
window1.title('Login')
def a():
	window1.destroy()
myfont = font.Font(family='Helvetica')
greeting = tk.Label(text="Login to your Account.", foreground='Green', background='Black', width=60, height=2)
label1 = tk.Label(text="Email-Id")
label2 = tk.Label(text="Password")
user1 = tk.Entry(text='Username', bg='Black', fg='Green')
user1['font'] = myfont
password1 = tk.Entry(text='Password', bg='black', fg='Green')
password1['font'] = myfont
def c(user1,password1):
	global user
	global password
	user=user1.get()
	password=password1.get()

button = tk.Button(text="Login", foreground='Yellow', background='Red',command=lambda:[c(user1,password1),a(),main_page()])
button['font'] = myfont
greeting.pack()
label1.pack()
user1.pack()
label2.pack()
password1.pack()
button.pack()
window1.mainloop()