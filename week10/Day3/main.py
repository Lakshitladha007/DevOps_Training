import paramiko
import smtplib
import os
from dotenv import load_dotenv

def send_email(custom_message):
    load_dotenv() 
    email_passcode=os.getenv("email_passcode")
    sender_email=os.getenv("sender_email")
    receiver_email=os.getenv("receiver_email")
    subject="Disk usage Alert"
    message=custom_message
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


def check_remote_disk_usage():

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to Remote Server")
    try: 
        client.connect(
            hostname="52.138.52.113", 
            port=22,
            username="azureuser",
            key_filename=r"C:\cprogramming\my-key.pem")

        stdin, stdout, stderr = client.exec_command(f"df -h /")
        output = stdout.read().decode()
        error = stderr.read().decode()
        lines = output.splitlines()
        if len(lines) > 1:
            usage = lines[1].split()
            percent_used = int(usage[4].replace('%', ''))
            custom_message=None
            if percent_used > 75:
                custom_message="WARNING: Disk usage above 75%"
                send_email(custom_message)
            else:
                custom_message="OK: Disk usage is within safe limits"
                send_email(custom_message)

    except Exception:
        print(f"SSH connection failed: {Exception}")
    finally:
        client.close()


if __name__ =="__main__":
    check_remote_disk_usage()