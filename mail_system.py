import os, smtplib
from email.message import EmailMessage
from email.utils import formataddr

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "25"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_USE_TLS = os.getenv("SMTP_USE_TLS", "false").lower() == "true"
MAIL_FROM = os.getenv("MAIL_FROM", SMTP_USER or "no-reply@example.com")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME", "Terraforming Mars")

def send_registration_email(to_email: str, username: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = "Welcome to Terraforming Mars Leagues 🚀"
    msg["From"] = formataddr((MAIL_FROM_NAME, MAIL_FROM))
    msg["To"] = to_email
    msg.set_content(
        f"Hi {username},\n\n"
        "Welcome aboard! Your account has been created successfully.\n"
        "You can now log in and start tracking your games.\n\n"
        "— Terraforming Mars Leagues Team"
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as smtp:
        smtp.ehlo() 
        if SMTP_USE_TLS:
            smtp.starttls()
            smtp.ehlo()
        if SMTP_USER and SMTP_PASS:
            smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)
