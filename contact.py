import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
TO_EMAIL = os.getenv("TO_ADDRESS", "ahavatolamglobalfarm@gmail.com")


def send_email(name, company, email, message):
    """
    Send contact form email using SendGrid API.
    Returns {"success": True} or {"error": "..."}
    """

    if not all([name, email, message]):
        return {"error": "Missing required fields (name, email, message)"}

    subject = f"New Contact Form from {name}"
    content = f"Name: {name}\nCompany: {company}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        mail = Mail(
            from_email=email,
            to_emails=TO_EMAIL,
            subject=subject,
            plain_text_content=content
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(mail)
        return {"success": True}

    except Exception as e:
        return {"error": f"SendGrid error: {str(e)}"}