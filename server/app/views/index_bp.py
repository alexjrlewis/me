"""Module containing the blueprint for the API."""

from flask import Blueprint, jsonify, render_template, request

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", methods=["GET"])
def get():
    return render_template("index.html")
