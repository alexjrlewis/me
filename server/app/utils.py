"""Module containing email helper functions."""

from threading import Thread
from typing import Dict, Optional
from flask import current_app
from flask_mail import Message
import html2text  # courtesy of https://en.wikipedia.org/wiki/Aaron_Swartz

from app import mail

def _send_async_email(app, message: Message):
    """Send a message on a different thread using magic to pass the app to that
    tread, see:

        https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
    
    Args:
        app: The real application instance that is stored inside the proxy
            object, current_app.
        message: The message to send.
    """
    with app.app_context():
        mail.send(message)

def send_email(recipient: str, subject: str, html_body: str,
               attachment: Optional[Dict[str, str]] = None):
    """Sends an email to a recipient from the default mail sender.

    Args:
        recipient: The recipient of the email.
        subject: The subject of the email.
        html_body: The HTML mark up of the email.
        attachment: An optional dictionary representing an attachment with the
            following keys:
                'filename': the filename of the attachment.
                'content_type': file MIME type, application/pdf.
                'data': the raw file data.
                'disposition': the content disposition.
    """
    text_body = html2text.html2text(html_body) # convert to plain text message of the email.
    message = Message(subject, recipients=[recipient], html=html_body,
                      # bcc='',
                      body=text_body)
    if attachment:
        message.attach(**attachment)
    args = (current_app._get_current_object(), message)
    thread = Thread(target=_send_async_email, args=args)
    thread.start()
