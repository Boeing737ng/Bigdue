import os
import csv
import datetime, time
from flask import Flask, request, session, g, redirect, url_for, abort, \
                  render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_motion():
    entries = list()
    with open('csvfile/src.csv', 'r') as csvfile:
        motionreader = csv.DictReader(csvfile, quotechar = '\"')
        for row in motionreader:
            entries.append((row['ipaddress'], row['date'],  row['date'], row['data size'], row['count']))
    return render_template('motion_chart.html', entries = entries)
