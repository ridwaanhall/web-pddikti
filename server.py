from flask import Flask, render_template, request
from Controller.AllController import COLLEGE, STUDY_PROGRAMS, PROVINCES, STUDENTS, SEARCH_OTHER

app = Flask(__name__)


# ============== HOME =========================
@app.route('/')
def dashboard():
  return render_template('dashboard.html')


# =============== LECTURER =======================
@app.route("/search-lecturers", methods=["GET", "POST"])
def search_lecturers():
  lecturers = []
  search_name = None  # Initialize search_name here

  if request.method == "POST":
    search_name = request.form.get("search_name")
    if search_name:
      lecturers = SEARCH_OTHER().GetDsnList(search_name)
  else:
    lecturers = SEARCH_OTHER().GetDsnList()

  print("HEHE", lecturers)
  print("searchhh", search_name)
  return render_template("search-lecturers.html",
                         lecturers=lecturers,
                         search_name=search_name)


# =============== STUDENTS =======================
@app.route("/search-students", methods=["GET", "POST"])
def search_students():
  students = []
  search_name = None  # Initialize search_name here

  if request.method == "POST":
    search_name = request.form.get("search_name")
    if search_name:
      students = STUDENTS().GetMhsList(search_name)
  else:
    students = STUDENTS().GetMhsList()

  #print("HEHE", students)
  #print("searchhh", search_name)
  return render_template("search-students.html",
                         students=students,
                         search_name=search_name)


@app.route('/detail-student')
def detail_student():
  default_student_details = {"dataumum": {"nm_pd": "No Student Selected"}}
  return render_template('detail-student.html',
                         student_details=default_student_details)


@app.route("/detail-student/<student_id>")
def detail_student_id(student_id):
  students = STUDENTS()
  student_details = students.GetStudentDetail(student_id)
  return render_template("detail-student.html",
                         student_id=student_id,
                         student_details=student_details)


# ============ COLLEGES ==============================
@app.route("/colleges")
def colleges():
  colleges = COLLEGE()
  college_list = colleges.CollegeList()
  print('ridddddddd', college_list)
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
