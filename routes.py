from flask import Flask, render_template, request
from threading import Thread
import sys
import os
import main
import export_csv_file

app = Flask(__name__)      

def getTimestamp():
  timestamp = export_csv_file.export_csv_file()
  timestamp_array = timestamp.time_list
  return timestamp_array

@app.route('/')
def home():
  time = getTimestamp()
  return render_template('home.html', title = 'Main', accessRoot = time)

@app.route('/graph')
def graph():
  return render_template('graph.html')

@app.route('/map')
def map():
  time = getTimestamp()
  return render_template('map.html', title = 'Map', accessRoot = time)

@app.route('/bubble')
def bubble():
  return render_template('bubble.html', title = 'Buuble')

@app.route('/timeGraph')
def timeGraph():
  return render_template('timeGraph.html', title = 'Time - Graph')

@app.route('/sendValue', methods=['POST'])
def getTimeValue():
  print('yes')
  time = request.form.get('value')
  #time = request.args.get('value') # For 'GET' method
  #main.main(time)
  print(time)
  return 'done'

if __name__ == '__main__':
  t1 = Thread(target = main.main)
  t1.setDaemon(True)
  t1.start()

  t2 = Thread(target = app.run)
  t2.setDaemon(True)
  t2.start()
  while True:
     pass
  #app.run(debug=True)