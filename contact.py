import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

# Email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))  # Ensure integer
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS", "ahavatolamglobalfarm@gmail.com")


def send_email(name, company, email, message):
    """
    Send an email from the contact form.
    Returns a dict:
        {"success": True}  OR  {"error": "error message"}
    """

    # Validate required fields
    if not all([name, email, message]):
        return {"error": "Missing required fields (name, email, message)"}

    # Build email content
    subject = f"New Contact Form from {name}"
    body = f"Name: {name}\nCompany: {company}\nEmail: {email}\n\nMessage:\n{message}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_ADDRESS

    try:
        # Connect and send email using SSL
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return {"success": True}

    except smtplib.SMTPAuthenticationError:
        return {"error": "SMTP authentication failed. Check your email credentials."}

    except smtplib.SMTPConnectError:
        return {"error": "Could not connect to the SMTP server."}

    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"Unexpected error: {str(e)}"}