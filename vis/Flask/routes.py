from flask import Flask, render_template
import test

app = Flask(__name__)      
 
@app.route('/')
def home():
  test.foo()
  return render_template('home.html', title = 'Main')

@app.route('/graph')
def graph():
  return render_template('graph.html', title = 'graph')
 
if __name__ == '__main__':
  app.run(debug=True)