from flask import Flask, render_template
from Controller.AllController import COLLEGE, STUDY_PROGRAMS, PROVINCES

app = Flask(__name__)


# ============== HOME =========================
@app.route('/')
def dashboard():
  return render_template('dashboard.html')


# =============== STUDENTS =======================
@app.route("/search-students")
def search_students():
  return render_template("search-students.html")

# ============ COLLEGES ==============================
@app.route("/colleges")
def colleges():
  colleges = COLLEGE()
  college_list = colleges.CollegeList()
  return render_template("colleges.html", college_list=college_list)


# ================= STUDY PROGRAMS ===================
@app.route("/study-programs")
def study_programs():
  studyprograms = STUDY_PROGRAMS()
  studyprograms_list = studyprograms.StudyProgramsList()
  return render_template("study-programs.html",
                         studyprograms_list=studyprograms_list)


# ================= PROVINCES ========================
@app.route("/provinces")
def provinces():
  provinces = PROVINCES()
  provinces_list = provinces.ProvincesList()
  return render_template("provinces.html", provinces_list=provinces_list)
