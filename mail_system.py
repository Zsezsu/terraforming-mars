from flask import Blueprint

mail = Blueprint('mail_system', __name__, template_folder='templates')


def send_registration_email():
    pass
