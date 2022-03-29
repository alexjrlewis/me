"""Module containing the pay form."""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SelectField, DecimalField, TextAreaField, SubmitField
import wtforms.validators as validators


class PayForm(FlaskForm):

    amount = DecimalField(
        "Amount",
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "1,000", "class": "u-full-width"},
    )

    currency = SelectField(
        "Select a currency",
        choices=[
            ("sats", "Sats"),
            ("btc", "₿"),
            ("gbp", "£"),
            ("usd", "$"),
            ("eur", "€"),
        ],
        render_kw={"class": "u-full-width"},
    )

    memo = TextAreaField(
        "Memo",
        [validators.optional(), validators.length(max=200)],
        default="please add content",
        render_kw={"placeholder": "Invoice for …", "class": "u-full-width"},
    )

    recaptcha = RecaptchaField()

    submit = SubmitField("Generate", render_kw={"class": "button-primary"},)
