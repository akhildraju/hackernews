# web_app/routes/home_routes.py

from flask import Blueprint, render_template
from web_app.models import DB, Record


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def root():
    records = Record.query.all()

    return render_template("records.html", message="Here are the records", records=records)

@home_routes.route("/about")
def about():
    return "Akhil Raju's Dashboard "
