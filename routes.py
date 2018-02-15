import sys
import os
import json
from flask import Flask, render_template, request, jsonify
from threading import Thread
from app.bigdue_app import main
from app.bigdue_app import Export_csv_file
from app.makecsv import main as maincsv
from app.makecsv import Read_packet

app = Flask(__name__)      

def get_csv_list():
  csvlist = list()
  file_path = os.getcwd()+'/static/data/packet/'
  for file in os.listdir(file_path):
    if file.endswith('.csv'):
        csvlist.append(file)

  csvlist.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
  return csvlist

@app.route('/')
def home():
  timestamp_array = get_csv_list()
  
  first = request.args.get('first')
  last = request.args.get('last')
  timestamp = request.args.get('current_timestamp')
  
  if not timestamp == None:
    print("start: " + first + ", " + "end: " + last + ", " + "filename: " + timestamp)
    maincsv.main([first, last, timestamp])

  return render_template('home.html', title = 'Main', timestamp = timestamp_array)

@app.route('/graph')
def graph():
  return render_template('graph.html', title = 'Graph')

@app.route('/map')
def map():
  return render_template('map.html', title = 'Map')

@app.route('/bubble')
def bubble():
  return render_template('bubble.html', title = 'Bubble')

@app.route('/timeGraph')
def timeGraph():
  return render_template('timeGraph.html', title = 'Time - Graph')

if __name__ == '__main__':
  t1 = Thread(target = main.main)
  t1.setDaemon(True)
  t1.start()

  t2 = Thread(target = app.run)
  t2.setDaemon(True)
  t2.start()
  while True:
    if not t1.isAlive():
      sys.exit(0)
    pass
  #app.run(debug=True)