import smtplib
def prin():
    print(a)

def sendmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("your_email", "your_password")
    server.sendmail(
    "from_email", 
    "to_email", 
    "text")
    server.quit()

err = 0
while True:
    try:
        prin()
    except:
        err = err + 1
        if err == 1:
            sendmail()
            exit()