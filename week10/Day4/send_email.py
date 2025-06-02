import smtplib
import os
import logging
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    filename='email_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email():
    load_dotenv() 
    email_passcode = os.getenv("email_passcode")
    sender_email = os.getenv("sender_email")
    receiver_email = os.getenv("receiver_email")
    subject = "Disk usage Alert"
    message = "Hello this is a testing mail"
    text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, email_passcode)
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        print(f"Error: {e}")
    else:
        logging.info("Email sent successfully.")
        print("Email notification sent successfully.")
    finally:
        try:
            server.quit()
        except:
            pass

if __name__ == "__main__":
    send_email()
