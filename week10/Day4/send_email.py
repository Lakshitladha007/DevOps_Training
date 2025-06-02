import smtplib
import os
from dotenv import load_dotenv

def send_email():
    load_dotenv() 
    email_passcode=os.getenv("email_passcode")
    sender_email=os.getenv("sender_email")
    receiver_email=os.getenv("receiver_email")
    subject="Disk usage Alert"
    message="Hello this is a testing mail"
    text=f"Subject: {subject}\n\n{message}"
    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, email_passcode)
        server.sendmail(sender_email, receiver_email, text)
    except Exception:
        print(Exception)
    else:
        print("Email notification sent successfully")
    finally:
        server.quit()


if __name__ =="__main__":
    send_email()