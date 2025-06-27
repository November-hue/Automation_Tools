import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = "novstechsa@gmail.com.com"
    receiver = "receiver@example.com"
    subject = "Automated Message"
    body = "This is an automated email from AutoTasker."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, "your_password")
            server.send_message(msg)
        print("Email sent successfully.\n")
    except Exception as e:
        print(f"Email failed: {e}\n")
