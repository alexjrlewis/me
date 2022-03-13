"""Module containing the blueprint for webhooks."""

import getpass
import hashlib
import hmac
import json
import six
import subprocess
from flask import Blueprint, jsonify, request
from flask import current_app as app

webhooks_bp = Blueprint("webhooks_bp", __name__)


@webhooks_bp.route("/github", methods=["POST"])
def github():
    """Triggered when a push request is made to Github."""
    try:
        secret = app.config["GITHUB_WEBHOOK_KEY"].encode("utf-8")
        digest = six.text_type(hmac.new(secret, request.data, hashlib.sha1).hexdigest())
        sig_parts = request.headers["X-Hub-Signature"].split("sha1=")
        if not hmac.compare_digest(sig_parts[1], digest):
            raise Exception("GITHUB_WEBHOOK_KEY does not match.")
    except Exception as e:
        return jsonify({"error": e}), 400
    # try:
    #     result = subprocess.run(['bash', 'update'],
    #                             cwd=f'/home/{getpass.getuser()}/deployment_manager/scripts',
    #                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # except Exception as e:
    #     return jsonify({'error': e}), 400
    # else:
    #     return jsonify({'status': 'success'}), 200
