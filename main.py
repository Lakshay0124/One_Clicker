import smtplib, ssl


port = 465
smtp_server = "smtp.gmail.com"


a = "yes"
if a == "yes":

    with open("your_mail.txt", "r") as c:
        sender = c.read()

    with open("receiver.txt", "r") as d:
        getter = d.read()

    with open("password.txt", "r") as e:
        password = e.read()

    with open("message.txt", "r") as f:
        messagepre = f.read()



context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, getter, messagepre)
