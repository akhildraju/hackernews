from flask import Blueprint, render_template
import pandas as pd
import os

from web_app.models import DB, Record

loaddata_routes = Blueprint("loaddata_routes", __name__)

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "hackernews.csv")

@loaddata_routes.route("/loaddata")
def refresh():
    """Load data from CSV and Save it in the database."""
    DB.drop_all()
    DB.create_all()

    df = pd.read_csv(CSV_FILE_PATH)

    counter = 0
    for row in df.values:
        # print (row)
        record = Record()
        record.row_id = row[0]
        record.by = row[1]
        record.id = row[2]
        record.kids = row[3]
        record.parent = row[4]
        record.text = row[5]
        record.time = row[6]
        record.type = row[7]
        record.title = row[8]
        record.url = row[9]
        record.vader_score = row[10]
        record.neg_score = row[11]
        DB.session.add(record)

        counter +=  1
        

    DB.session.commit()
    return "Successfully inserted " + str(counter) + " records"
