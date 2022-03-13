"""Module containing the blueprint for the API."""

from flask import Blueprint, jsonify, render_template, request

# from app import lnnode
from app import qrcode
from app.forms.pay_form import PayForm


pay_bp = Blueprint("pay_bp", __name__)

def payment_request_to_html(payment_request: str, n: int = 10) -> str:
    """

    Args:
        payment_request:
        n:
    Returns:
        .
    """
    return f"<b>{payment_request[:n]}</b>{payment_request[n:-n]}<b>{payment_request[-n:]}</b>"


def payment_request_to_qr(payment_request: str) -> str:
    """

    Args:
        payment_request:
        n:
    Returns:
        .
    """
    return qrcode(payment_request)


@pay_bp.route("/", methods=["GET", "POST"])
def get():
    form = PayForm()
    payment_request = "lntb10m1pwr6x4spp57r8y5aslqnrmaap0cv3uefy9puchccjzre5k2nl2f4s9uuxr8xeqdqqcqzysxqzjc4ssgpuk27qesndex0sna6e33skjqwju5sd4ydcp0mnzctsvuq23sjst0wedlx9n6q0vj6md7auv7hjapdzu5qg5v34vfd6snwa5hnrqqnvhulk"
    payment_request_qrcode = payment_request_to_qr(payment_request)
    # payment_request_html = payment_request_to_html(payment_request)
    payment_request_html = payment_request
    payment_request_expiration_time = 600  # in seconds
    data = {
        "payment_request_html": payment_request_html,
        "payment_request_qrcode": payment_request_qrcode,
        "payment_request_expiration_time": payment_request_expiration_time,
        }
    return render_template("pay.html", form=form,
            payment_request_qrcode=payment_request_qrcode,
            payment_request_html=payment_request_html,
            payment_request_expiration_time=payment_request_expiration_time)


# https://alexjrlewis.me/pay/get-invoice-<amount>-<currency>
@pay_bp.route("/generate-invoice-<amount>-<currency>", methods=["GET"])
def test(amount: int, currency: str):
    pass


@pay_bp.route("/generate-invoice", methods=["POST"])
def generate_invoice():
    # generate-invoice-100-sats
    form = PayForm()
    if form.validate_on_submit():
        invoice = ""
        # invoice = lnnode.get_invoice(
        #     amount=form.amount, currency=form.currency, memo=form.memo
        # )
    return render_template("pay.html", form=form, invoice=invoice)
