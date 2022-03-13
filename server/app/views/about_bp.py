"""Module containing the blueprint for the API."""

from flask import Blueprint, jsonify, render_template, request

about_bp = Blueprint("about_bp", __name__)


@about_bp.route("/", methods=["GET"])
def get():
    return render_template("about.html")
