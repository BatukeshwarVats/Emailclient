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

def showinbox():
    temp=open('inbox.txt','r')
    window=tk.Tk()
    window.geometry("1280x500")
    window.title('Inbox')
    sb=Scrollbar(window)
    sb.pack(side=RIGHT,fill=Y)
    def g():
        window.destroy()
    mylist=Listbox(window,yscrollcommand=sb.set,width=140,font=(None,12),height=50)
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',font=(None,15),height=2,command=lambda: [g(),main_page()])
    greeting = tk.Label(text="Inbox", foreground='Green', background='Black',font=(None,17),width=80,height=2)
    greeting.pack()
    back_button.place(x=0.0)
    for i in temp:
        mylist.insert(END,i)
    mylist.pack(pady=2.0,side=LEFT)
    sb.config(command=mylist.yview)
    window.mainloop()

def showsent():
    temp=open('inbox.txt','r')
    window=tk.Tk()
    window.geometry("1280x500")
    window.title('Sent Box')
    sb=Scrollbar(window)
    sb.pack(side=RIGHT,fill=Y)
    def g():
        window.destroy()
    mylist=Listbox(window,yscrollcommand=sb.set,width=140,font=(None,12),height=50)
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',font=(None,15),height=2,command=lambda: [g(),main_page()])
    greeting = tk.Label(text="Sent Box", foreground='Green', background='Black',font=(None,17),width=80,height=2)
    greeting.pack()
    back_button.place(x=0.0)
    for i in temp:
        mylist.insert(END,i)
    mylist.pack(pady=2.0,side=LEFT)
    sb.config(command=mylist.yview)
    window.mainloop()

#batukeshwar
def  sent_successfully():
    myfont = font.Font(family='Helvetica')
    window4=tk.Tk()
    window4.title("Mail sent")
    label4=tk.Label(text='Your mail has been sent sucessfully',fg='Green',bg='Black',font=(None,15),width=50,height=10)
    label4.pack()
    def e():
        window4.destroy()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',command=lambda: [e(), main_page()])
    back_button['font'] = myfont
    back_button.pack()
#suhail
def  logout_successfully():
    window1 = tk.Tk()
    window1.title('Login')

    def a():
        window1.destroy()

    myfont = font.Font(family='Helvetica')
    greeting1 = tk.Label(text="You have successfully logged out.", foreground='Green', background='Black',font=(None, 15), width=40, height=2)
    greeting2 = tk.Label(text="Login to another account.", foreground='Green', background='Black',font=(None, 15), width=40, height=2)
    label1 = tk.Label(text="Email-Id", font=(None, 15), width=40, height=2)
    label2 = tk.Label(text="Password", font=(None, 15), width=40, height=2)
    user1 = tk.Entry(text='Username', bg='Black', fg='Green', width=35)
    user1['font'] = myfont
    password1 = tk.Entry(text='Password', bg='black', fg='Green', width=35)
    password1['font'] = myfont

    def c(user1, password1):
        global user
        global password
        user = user1.get()
        password = password1.get()
        # def l():
        session2 = imaplib.IMAP4_SSL(reciever_host)
        try:
            k = session2.login(user, password)[0]
            a()
            main_page()
        except:
            a()
            login2()

    button = tk.Button(text="Login", foreground='Yellow', background='Red', command=lambda: [c(user1, password1)])

    button['font'] = myfont
    greeting1.pack()
    greeting2.pack()
    label1.pack()
    user1.pack()
    label2.pack()
    password1.pack()
    button.pack()
    window1.mainloop()

#ashwani singh
def error1():
    myfont = font.Font(family='Helvetica')
    window3=tk.Tk()
    window3.title("Error")
    label3=tk.Label(text='Sorry :(   Try again.',fg='Green',bg='Black',font=(None, 15),width=40,height=10)
    label3.pack()
    def e():
        window3.destroy()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',command=lambda: [e(), main_page()])
    back_button['font'] = myfont
    back_button.pack()
def error2():
    myfont = font.Font(family='Helvetica')
    window3=tk.Tk()
    window3.title("Error")
    label3=tk.Label(text='Sorry :(   Try again.',fg='Green',bg='Black',font=(None, 15),width=40,height=10)
    label3.pack()
    def e():
        window3.destroy()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',command=lambda: [e(), login1()])
    back_button['font'] = myfont
    back_button.pack()

def error3():
    myfont = font.Font(family='Helvetica')
    window3=tk.Tk()
    window3.title("Cleared")
    label3=tk.Label(text='Sorry :(   Try again.',fg='Green',bg='Black',font=(None, 15),width=40,height=10)
    label3.pack()
    def e():
        window3.destroy()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',command=lambda: [e(), main_page()])
    back_button['font'] = myfont
    back_button.pack()
#suhail


#ashwani garg
def del_all():
    myfont = font.Font(family='Helvetica')
    window5=tk.Tk()
    window5.title("Clear all")
    label5=tk.Label(text='You have cleared all from Inbox.',fg='Green',bg='Black',font=(None, 15),width=40,height=10)
    label5.pack()
    def e():
        window5.destroy()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',command=lambda: [e(), main_page()])
    back_button['font'] = myfont
    back_button.pack()

#ashwani garg
def compose_new():
    window = tk.Tk()
    window.title('Compose')
    greeting = tk.Label(text="Create new mail", foreground='Green', background='Black', width=60)
    myfont = font.Font(family='Helvetica')
    label5 = tk.Label(text="To")
    label6 = tk.Label(text="Subject")
    label7 = tk.Label(text="Body")
    reciever_id = tk.Entry(bg='pink', fg='green',width=40)
    entrysub = tk.Entry(bg='black', fg='green', width=50)
    entrymain = tk.Text(bg='black', fg='green', width=50, height=10)
    greeting['font'] = myfont
    reciever_id['font'] = myfont
    entrysub['font'] = myfont
    entrymain['font'] = myfont

    def g():
        window.destroy()

    def d(reciever_id, entrymain):
        global reciever
        reciever = reciever_id.get()
        #global sub
        #sub=entrysub.get()
        global msg1
        msg1 = entrymain.get("1.0", 'end-1c')
        g()
    sendmail = tk.Button(text="Send", foreground='Yellow', background='Red',
                         command=lambda: [d(reciever_id, entrymain), compose2()])

    sendmail['font'] = myfont
    greeting.pack()
    label5.pack()
    reciever_id.pack()
    label6.pack()
    entrysub.pack()
    label7.pack()
    entrymain.pack()
    sendmail.pack()
    back_button = tk.Button(text="Go Back", foreground='Yellow', background='Red',
                            command=lambda: [g(),main_page()])
    back_button['font']=myfont
    back_button.pack()
    window.mainloop()

#batukeshwar vats
def main_page():
    root = tk.Tk()
    root.title('Homepage')

    def b():
        root.destroy()

    greeting = tk.Label(text="Welcome to Homepage", foreground='Green', background='Black', width=60, height=2,font=(None,15))
    greeting.pack()
    topFrame = Frame(root)
    topFrame.pack()
    myfont = font.Font(family='Helvetica')
    create = tk.Button(topFrame, text='Compose', bg='Red', fg='green', width=50, command=lambda: [b(), compose_new()])
    inbox = tk.Button(topFrame, text='Inbox', bg='Red', fg='green', width=50, command=lambda:[b(),read_inbox()])
    sent = tk.Button(topFrame, text='Sent', bg='Red', fg='green', width=50, command=lambda :[b(),read_sent()])
    delete_all_read = tk.Button(topFrame, text='Delete all unseen', bg='Red', fg='green', width=50,command=lambda:[b(),delete_unseen()])
    delete_all = tk.Button(topFrame, text='Delete all', bg='Red', fg='green', width=50, command=lambda:[b(),delete_all_inbox()])
    logout = tk.Button(text="Logout", foreground='Yellow', background='Red', command=lambda:[b(),logout_account()])
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
#batukeshwarvats
def main_page2():
    root = tk.Tk()
    root.title('Homepage')

    def b():
        root.destroy()

    greeting1 = tk.Label(text="All unread cleared", foreground='Green', background='Black', width=60, height=2,font=(None,15))
    #greeting2 = tk.Label(text="Welcome to Homepage", foreground='Green', background='Black', width=60, height=2,font=(None,15))
    greeting1.pack()
    #greeting2.pack()
    topFrame = Frame(root)
    topFrame.pack()
    myfont = font.Font(family='Helvetica')
    create = tk.Button(topFrame, text='Compose', bg='Red', fg='green', width=50, command=lambda: [b(), compose_new()])
    inbox = tk.Button(topFrame, text='Inbox', bg='Red', fg='green', width=50, command=read_inbox)
    sent = tk.Button(topFrame, text='Sent', bg='Red', fg='green', width=50, command=read_sent)
    delete_all_read = tk.Button(topFrame, text='Delete all unseen', bg='Red', fg='green', width=50,command=lambda:[b(),delete_unseen()])
    delete_all = tk.Button(topFrame, text='Delete all', bg='Red', fg='green', width=50, command=lambda:[b(),delete_all_inbox()])
    logout = tk.Button(text="Logout", foreground='Yellow', background='Red', command=lambda:[b(),logout_account()])
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
#batukeshwar vats
def main_page3():
    root = tk.Tk()
    root.title('Homepage')

    def b():
        root.destroy()

    greeting1 = tk.Label(text="Inbox cleared", foreground='Green', background='Black', width=60, height=2,font=(None,15))
    #greeting2 = tk.Label(text="Welcome to Homepage", foreground='Green', background='Black', width=60, height=2,font=(None,15))
    greeting1.pack()
    #greeting2.pack()
    topFrame = Frame(root)
    topFrame.pack()
    myfont = font.Font(family='Helvetica')
    create = tk.Button(topFrame, text='Compose', bg='Red', fg='green', width=50, command=lambda: [b(), compose_new()])
    inbox = tk.Button(topFrame, text='Inbox', bg='Red', fg='green', width=50, command=read_inbox)
    sent = tk.Button(topFrame, text='Sent', bg='Red', fg='green', width=50, command=read_sent)
    delete_all_read = tk.Button(topFrame, text='Delete all unseen', bg='Red', fg='green', width=50,command=lambda:[b(),delete_unseen()])
    delete_all = tk.Button(topFrame, text='Delete all', bg='Red', fg='green', width=50, command=lambda:[b(),delete_all_inbox()])
    logout = tk.Button(text="Logout", foreground='Yellow', background='Red', command=lambda:[b(),logout_account()])
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
#ashwani singh
def login1():
    window1 = tk.Tk()
    window1.title('Login')

    def a():
        window1.destroy()

    myfont = font.Font(family='Helvetica')
    greeting = tk.Label(text="Login to your Account.", foreground='Green', background='Black',font=(None,15),width=40,height=2)
    label1 = tk.Label(text="Email-Id",font=(None,15),width=40,height=2)
    label2 = tk.Label(text="Password",font=(None,15),width=40,height=2)
    user1 = tk.Entry(text='Username', bg='Black', fg='Green',width=35)
    user1['font'] = myfont
    password1 = tk.Entry(text='Password', bg='black', fg='Green',width=35)
    password1['font'] = myfont

    def c(user1, password1):
        global user
        global password
        user = user1.get()
        password = password1.get()
        session2 = imaplib.IMAP4_SSL(reciever_host)
        try:
            k=session2.login(user, password)[0]
            a()
            main_page()
        except:
            a()
            login2()


    button = tk.Button(text="Login", foreground='Yellow', background='Red',width=10,command=lambda: [c(user1, password1), a(), main_page()])

    button['font'] = myfont
    greeting.pack()
    label1.pack(ipady=3)
    user1.pack(ipady=3)
    label2.pack(ipady=3)
    password1.pack(ipady=3)
    button.pack(ipady=3)
    window1.mainloop()



#batukeshwarvats
def login2():
    window1 = tk.Tk()
    window1.title('Login')

    def a():
        window1.destroy()

    myfont = font.Font(family='Helvetica')
    greeting = tk.Label(text="  :(  Enter correct credentials.", foreground='Green', background='Black',font=(None,15),width=40,height=2)
    label1 = tk.Label(text="Email-Id",font=(None,15),width=40,height=2)
    label2 = tk.Label(text="Password",font=(None,15),width=40,height=2)
    user1 = tk.Entry(text='Username', bg='Black', fg='Green',width=35)
    user1['font'] = myfont
    password1 = tk.Entry(text='Password', bg='black', fg='Green',width=35)
    password1['font'] = myfont

    def c(user1, password1):
        global user
        global password
        user = user1.get()
        password = password1.get()
    #def l():
        session2 = imaplib.IMAP4_SSL(reciever_host)
        try:
            k=session2.login(user, password)[0]
            a()
            main_page()
        except:
            a()
            login2()


    button = tk.Button(text="Login", foreground='Yellow', background='Red',command=lambda:[c(user1,password1)])

    button['font'] = myfont
    greeting.pack()
    label1.pack()
    user1.pack()
    label2.pack()
    password1.pack()
    button.pack()
    window1.mainloop()


#ashwani singh
def compose2():
    try:
        session = smtplib.SMTP(sender_host, 587)
        session.starttls()
        session.login(user, password)
        session.sendmail(user, reciever, msg1)
        compose_new()
        session.quit()
    except:
        error1()

#batukeshwar
def read_inbox():
    try:
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        status, message = session2.select('Inbox')
        N = 5

        message = int(message[0])
        temp=open('inbox.txt','w')
        for i in range(message, message - N, -1):
            res, msg2 = session2.fetch(str(i), "(RFC822)")
            for response in msg2:
                if isinstance(response, tuple):
                    msg2 = email.message_from_bytes(response[1])
                    subject = decode_header(msg2["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    from_ = msg2.get("From")
                    temp.write("%s\n" % "From:")
                    temp.write("%s\n" % from_)
                    temp.write("%s\n" % "Subject:")
                    temp.write("%s\n" % subject)
                    temp.write("%s\n" % "*************************************")
        temp.close()
        showinbox()
    except:
        error1()

#suhail
def logout_account():
    try:
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        print("Hello")
        logout_successfully()
    except:
        error1()

#suhail
def delete_unseen():
    try:
        session = IMAPClient(reciever_host, ssl=True, port=993)
        session.login(user, password)
        session.select_folder('Inbox')
        delmail = session.search('UNSEEN')
        session.delete_messages(delmail)
        main_page2()
    except:
        error1()

#ashwani garg
def delete_all_inbox():
    try:
        session = IMAPClient(reciever_host, ssl=True, port=993)
        session.login(user, password)
        session.select_folder('Inbox')
        delmail = session.search('ALL')
        session.delete_messages(delmail)
        main_page3()
    except:
        error1()

#ashwani signh
def read_sent():
    try:
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        status, message = session2.select('"[Gmail]/Sent Mail"')
        N = 5
        temp=open('sent.txt','w')
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
                    temp.write("%s\n" % "To")
                    temp.write("%s\n" % To)
                    temp.write("%s\n" % "Bcc:")
                    temp.write("%s\n" % Bcc)
                    temp.write("%s\n" % "Subject")
                    temp.write("%s\n" % subject)
                    temp.write("%s\n" % "*************************************")

        temp.close()
        showsent()

    except:
        error1()

login1()


