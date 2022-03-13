"""Module containing the pay form."""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, SelectField, SubmitField, StringField, TextAreaField
import wtforms.validators as validators


class ContactForm(FlaskForm):

    email = StringField(
        "Your email",
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "email@address.com", "class": "u-full-width"},
    )

    subject = SelectField(
        "Select a subject",
        choices=[
            ("hello", "Hello"),
            ("work", "Work"),
        ],
        render_kw={"class": "u-full-width"},
    )

    message = TextAreaField(
        "Message",
        [validators.DataRequired(), validators.length(max=200)],
        render_kw={"placeholder": "Hello …", "class": "u-full-width"},
    )

    should_copy_sender = BooleanField(
        "Send a copy to yourself?",
        validators=[
            validators.DataRequired(),
        ],
    )

    recaptcha = RecaptchaField()

    submit = SubmitField("Send")
