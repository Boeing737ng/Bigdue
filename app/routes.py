from flask import Flask, render_template
from threading import Thread
import sys
import os
import main
import export_csv_file
import html.parser as htmlparser

app = Flask(__name__)      

@app.route('/')
def home():
  return render_template('home.html', title = 'Main')

@app.route('/graph')
def graph():
  timestamp = export_csv_file.export_csv_file()
  timestamp_array = timestamp.time_list
  return render_template('graph.html', accessRoot = timestamp_array)
 
@app.route('/map')
def map():
  return render_template('map.html', title = 'Map')
if __name__ == '__main__':
  #t1 = Thread(target = main.main)
  t2 = Thread(target = app.run)
  #t1.setDaemon(True)
  t2.setDaemon(True)
  #t1.start()
  t2.start()
  while True:
      pass
  #app.run(debug=True)