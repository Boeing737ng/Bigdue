# all the imports
import os
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, \
                  render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_motion():
    entries = list()
#    with open('motion.csv', 'r') as csvfile:
#        motionreader = csv.DictReader(csvfile, quotechar = '\'')
    entries.append("['Apples',  new Date (1988,0,1), 1000, 300, 'East'],")
    entries.append("['Oranges', new Date (1988,0,1), 1150, 200, 'West'],")
    entries.append("['Bananas', new Date (1988,0,1), 300,  250, 'West'],")
    entries.append("['Apples',  new Date (1989,6,1), 1200, 400, 'East'],")
    entries.append("['Oranges', new Date (1989,6,1), 750,  150, 'West'],")
    entries.append("['Bananas', new Date (1989,6,1), 788,  617, 'West']")
    return render_template('motion_chart.html', entries = entries)
