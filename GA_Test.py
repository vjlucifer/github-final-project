import os
import smtplib
from email.message import EmailMessage

def send_test_email():
    # Retrieve credentials and details from environment variables
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 587))
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    recipient_email = os.environ.get("RECIPIENT_EMAIL")

    if not all([sender_email, sender_password, recipient_email]):
        raise ValueError("Missing required environment variables for email sending.")

    # Create the email message
    msg = EmailMessage()
    msg["Subject"] = "Test Email from GitHub Actions"
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(
        "Hello!\n\nThis is a test email sent automatically via GitHub Actions and Python."
    )

    # Connect to the server and send
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e

if __name__ == "__main__":
    send_test_email()
