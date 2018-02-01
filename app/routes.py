from flask import Flask, render_template
import sys
import os
#Root = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

import main
from csvFilter import csvFilter

app = Flask(__name__)      

@app.route('/')
def home():
  return render_template('home.html', title = 'Main')

@app.route('/graph')
def graph():
  #main.main(1)
  #csvFilter.main(1)
  return render_template('graph.html', title = 'Graph')
 
@app.route('/map')
def map():
  return render_template('map.html', title = 'Map')
if __name__ == '__main__':
  app.run(debug=True)