"""Module containing the blueprint for the API."""

from flask import Blueprint, jsonify, render_template, request
from app import mail
from app.forms.contact_form import ContactForm
contact_bp = Blueprint("contact_bp", __name__)


@contact_bp.route("/", methods=["GET"])
def get():
    form = ContactForm()
    return render_template("contact.html", form=form)


@contact_bp.route("/send-message", methods=["POST"])
def send_message():
    form = ContactForm()
    if form.validate_on_submit():
        print(form)
        msg = Message('Hello from the other side!', sender =   'peter@mailtrap.io', recipients = ['paul@mailtrap.io'])
        msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
        mail.send(msg)
        return "Message sent!"


