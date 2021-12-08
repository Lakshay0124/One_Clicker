import smtplib, ssl


port = 465
smtp_server = "smtp.gmail.com"


a = "yes"
if a == "yes":

    with open("your_mail.txt", "r") as c:
        sender = c.read()

    with open("receiver.txt", "r") as d:
        getter = d.read()

    with open("password_gmail.txt", "r") as e:
        password = e.read()

    with open("message.txt", "r") as f:
        messagepre = f.read()

    with open("receiver_2.txt", "r") as k:
        getter_2 = k.read()

    with open("receiver_3.txt", "r") as q:
        getter_3 = q.read()


with open("receiver_2.txt", "r") as v:
    content = v.read()
    for item in content:
        if ".com" in content:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, getter_2, messagepre)
                break
        else:
            print("no gmail provided in slot 2 ")
            break
with open("receiver_3.txt", "r") as v:
    content = v.read()
    for item in content:
        if ".com" in content:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, getter_3, messagepre)
                break
        else:
            print("no gmail provided in slot 3 ")
            break


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, getter, messagepre)
