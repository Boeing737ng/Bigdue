from flask import Flask, render_template
from Bigdue.app import main
import csvFilter

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html', title = 'Main')

@app.route('/graph')
def graph():
  csvFilter.main(1)
  main.main(1)
  return render_template('graph.html', title = 'graph')
 
if __name__ == '__main__':
  app.run(debug=True)