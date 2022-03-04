from flask import Blueprint
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

basedir = os.path.abspath(os.path.dirname(__file__))
text_file = os.path.join(basedir, 'templates/email-designs/test-mail.txt')
html_file = os.path.join(basedir, 'templates/email-designs/test-mail.html')

mail = Blueprint('mail_system', __name__, template_folder='templates')

mail_address = 'mars.scoreboard@gmail.com'
mail_password = 'ZsuBendeBenedekVik123#'


@mail.route('/mail-test')
def send_registration_email(customer_address=''):

    customer_address = 'dudaskobende@gmail.com'
    if not customer_address:
        print('customer email not found'
              'abort email sending'
              'see mail_system.py / send_registration_email() for more information')
        return ''
    print(f'customer email address: {customer_address}')

    # build email structure -----------------------------------------------
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Hello New User'
    msg['From'] = mail_address
    msg['To'] = customer_address

    # open files from templates/email-design route -------------------------
    with open(text_file, 'r') as plain_text:
        text = plain_text.read()
    with open(html_file, 'r') as design:
        html = design.read()

    # attach opened files to email structure -------------------------------
    mail_part_1 = MIMEText(text, 'plain')
    mail_part_2 = MIMEText(html, 'html')
    msg.attach(mail_part_1)
    msg.attach(mail_part_2)

    # login to GMAIL email system -----------------------------------------
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(mail_address, mail_password)

    # sends email and quit server -----------------------------------------
    try:
        server.sendmail(mail_address, customer_address, msg.as_string())
    except:
        print('An exception occurred when: email sent to client'
              '>-< Program skips step >-<'
              'see mail_system.py / send_registration_email() for more information')
    finally:
        server.quit()
    return ''
