from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/hehe')
def hehe():
  return "ini putri amanda K"