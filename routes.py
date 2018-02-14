import sys
import os
import json
from flask import Flask, render_template, request, jsonify
from threading import Thread
from app.bigdue_app import main
from app.bigdue_app import Export_csv_file
from app.makecsv import main as maincsv

app = Flask(__name__)      

def getTimestamp():
  timestamp = Export_csv_file.Export_csv_file()
  timestamp_array = timestamp.time_list
  return timestamp_array

@app.route('/')
def home():
  #time = getTimestamp()
  time = os.listdir(os.getcwd()+'/static/data/packet/')
  first = request.args.get('first')
  last = request.args.get('last')
  
  isExist = 'true' #For javascript
  if not first == None:
    isExist = 'false'
    print(first + ", " + last)
    maincsv.main([first, last])
  return render_template('home.html', title = 'Main', accessRoot = time, trigger = isExist)

@app.route('/graph')
def graph():
  return render_template('graph.html')

@app.route('/map')
def map():
  return render_template('map.html', title = 'Map', accessRoot = 'time')

@app.route('/bubble')
def bubble():
  return render_template('bubble.html', title = 'Buuble')

@app.route('/timeGraph')
def timeGraph():
  return render_template('timeGraph.html', title = 'Time - Graph')

  # @app.route('/sendValue')
# def home():
#   # print('yes')
#   # js_time = request.json('data') # For 'POST method
#   js_time = request.args.get('data') # For 'GET' method
#   # selected_time = json.loads(js_time)
#   print(js_time)
#   return render_template('index.html')

if __name__ == '__main__':
  # t1 = Thread(target = main.main)
  # t1.setDaemon(True)
  # t1.start()

  t2 = Thread(target = app.run)
  t2.setDaemon(True)
  t2.start()
  while True:
     pass
  #app.run(debug=True)