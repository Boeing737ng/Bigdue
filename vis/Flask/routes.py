from flask import Flask, render_template
import csvFilter

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html', title = 'Main')

@app.route('/graph')
def graph():
  csvFilter.main()
  return render_template('graph.html', title = 'graph')
 
if __name__ == '__main__':
  app.run(debug=True)