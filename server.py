from flask import Flask, render_template
from Controller.AllController import COLLEGE, STUDY_PROGRAMS, PROVINCES

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('datatable.html')


@app.route("/colleges")
def colleges():
  colleges = COLLEGE()
  college_list = colleges.CollegeList()
  return render_template("colleges.html", college_list=college_list)


@app.route("/study-programs")
def study_programs():
  studyprograms = STUDY_PROGRAMS()
  studyprograms_list = studyprograms.StudyProgramsList()
  return render_template("study-programs.html",
                         studyprograms_list=studyprograms_list)


@app.route("/provinces")
def provinces():
  provinces = PROVINCES()
  provinces_list = provinces.ProvincesList()
  return render_template("provinces.html",
                         provinces_list=provinces_list)
