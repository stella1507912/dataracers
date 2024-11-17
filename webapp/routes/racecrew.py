"""Routes for race event views for race crew members"""

from app import app
import queries.views as db
from collections import Counter
from flask import render_template, request, flash, redirect


@app.route("/race_crew")
def critical_dates():
    race_year = request.args.get("race_year")
    if race_year:
        data = db.critical_dates(race_year)
        stats = Counter([row[1] for row in data])
    else:
        data = None
        stats = None
    return render_template("views/critical_dates.jinja",
                           race_year=race_year, data=data, stats=stats)