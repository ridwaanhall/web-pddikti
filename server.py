from flask import Flask, render_template
from Controller.AllController import COLLEGE

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('dashboard.html')

@app.route("/colleges")
def colleges():
  colleges = COLLEGE()
  college_list = colleges.CollegeList()
  return render_template("colleges.html", college_list=college_list)