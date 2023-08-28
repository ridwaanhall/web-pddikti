from flask import Flask, render_template, request
from Controller.AllController import COLLEGE, STUDY_PROGRAMS, PROVINCES, STUDENTS, SEARCH_OTHER, LECTURERS

app = Flask(__name__)


# ============== HOME =========================
@app.route('/')
def dashboard():
  return render_template('dashboard.html')


# ========== LECTURERS ===================
@app.route('/detail-lecturer')
def detail_lecturer():
  default_lecturer_details = {"dataumum": {"nm_sdm": "No Lecturer Selected"}}
  return render_template('detail-lecturer.html',
                         lecturer_details=default_lecturer_details)


@app.route("/detail-lecturer/<lecturer_id>")
def detail_lecturer_id(lecturer_id):
  lecturer = LECTURERS()
  lecturer_details = lecturer.GetLecturerDetail(lecturer_id)
  return render_template("detail-lecturer.html",
                         lecturer_id=lecturer_id,
                         lecturer_details=lecturer_details)


# =============== SEARCH OTHER =======================
@app.route("/search-other", methods=["GET", "POST"])
def search_other():
  # HEAD
  lecturers = []
  studyprograms = []
  colleges = []

  search_name = None  # Initialize search_name here

  # lecturers, study programs
  if request.method == "POST":
    search_name = request.form.get("search_name")
    if search_name:
      lecturers = SEARCH_OTHER().GetDsnList(search_name)
      studyprograms = SEARCH_OTHER().GetProdiList(search_name)
      colleges = SEARCH_OTHER().GetPTList(search_name)
  else:
    lecturers = SEARCH_OTHER().GetDsnList()
    studyprograms = SEARCH_OTHER().GetProdiList()
    colleges = SEARCH_OTHER().GetPTList()

  return render_template("search-other.html",
                         lecturers=lecturers,
                         studyprograms=studyprograms,
                         colleges=colleges,
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


@app.route('/detail-college')
def detail_college():
  default_college_details = {
    "dataumum": {
      "nm_lemb": "No College Selected"
    },
    "akreditasi_list": [{
      "akreditasi": "No Data",
      "tgl_akreditasi": "No Data",
      "tgl_berlaku": "No Data"
    }]
  }
  return render_template('detail-college.html',
                         college_details=default_college_details)


@app.route('/detail-college/<college_id>')
def detail_college_id(college_id):
  college = COLLEGE()
  college_details = college.GetCollegeDetail(college_id)
  sp_details = college.GetSPDetail(college_id)
  return render_template("detail-college.html",
                         college_id=college_id,
                         college_details=college_details,
                         sp_details=sp_details)


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
