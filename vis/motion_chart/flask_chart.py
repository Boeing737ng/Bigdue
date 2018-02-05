import os
import csv
import datetime, time
from flask import Flask, request, session, g, redirect, url_for, abort, \
                  render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_motion():
    src_entries = list()
    dst_entries = list()
    with open('csvfile/src.csv', 'r') as srcfile, open('csvfile/dst.csv', 'r') as dstfile:
        src_motionreader = csv.DictReader(srcfile, quotechar = '\"')
        dst_motionreader = csv.DictReader(dstfile, quotechar = '\"')
        for row in src_motionreader:
            src_entries.append((row['ipaddress'], row['date'],  row['date'], row['data size'], row['count']))
        for row in dst_motionreader:
            dst_entries.append((row['ipaddress'], row['date'],  row['date'], row['data size'], row['count']))

    print(src_entries)
    print(dst_entries)
    return render_template('motion_chart.html', src_entries = src_entries, dst_entries =dst_entries)
