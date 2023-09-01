from flask import Flask, render_template, request
from Controller.AllController import COLLEGE, STUDY_PROGRAMS, PROVINCES, STUDENTS, SEARCH_OTHER, LECTURERS, DASHBOARD

app = Flask(__name__)


# ============== HOME =========================
@app.route('/')
def dashboard():
  dashboard = DASHBOARD()
  home_jumlah = dashboard.HomeJumlah()
  stat_prodi = dashboard.StatColProdi()
  stat_pt = dashboard.StatColPT()
  rerata_iku_keys, rerata_iku_values = dashboard.RerataCapaianIKU()
  mhs_bidang = dashboard.MhsBidang()
  dsn_klmn = dashboard.DsnKlmn()
  mhs_klmn = dashboard.MhsKlmn()
  dsn_pt = dashboard.DsnPt()
  dsn_ik = dashboard.DsnIk()
  pen_mhs = dashboard.PenMhs()

  # Pendidikan mahasiswa
  pen_mhs_series = pen_mhs['series'][0]['data']
  pen_mhs_keys = [item[0] for item in pen_mhs_series]
  pen_mhs_values = [item[1] for item in pen_mhs_series]
  
  # ikatan kerja dosen.
  dsn_ik_series = dsn_ik['series']
  dsn_ik_keys = [item['name'] for item in dsn_ik_series]
  dsn_ik_values = [item['data'][0] for item in dsn_ik_series]
  
  # pendidikan dosen.
  dsn_pt_series = dsn_pt['series']
  dsn_pt_keys = [item['name'] for item in dsn_pt_series]
  dsn_pt_values = [item['data'][0] for item in dsn_pt_series]
  
  # kelamin dosen.
  mhs_klmn_series = mhs_klmn['series']
  mhs_klmn_keys = [item['name'] for item in mhs_klmn_series]
  mhs_klmn_values = [item['data'][0] for item in mhs_klmn_series]
  
  # kelamin dosen.
  dsn_klmn_series = dsn_klmn['series']
  dsn_klmn_keys = [item['name'] for item in dsn_klmn_series]
  dsn_klmn_values = [item['data'][0] for item in dsn_klmn_series]
  
  # stat bidang name key and value
  mhs_bidang_series = mhs_bidang['series']
  mhs_bidang_keys = [item['name'] for item in mhs_bidang_series]
  mhs_bidang_values = [item['data'][0] for item in mhs_bidang_series]

  # stat prodi name key and value
  stat_prodi_series = stat_prodi['series']
  stat_prodi_keys = [item['name'] for item in stat_prodi_series]
  stat_prodi_values = [item['data'][0] for item in stat_prodi_series]

  # stat prodi name key and value
  stat_pt_series = stat_pt['series']
  stat_pt_keys = [item['name'] for item in stat_pt_series]
  stat_pt_values = [item['data'][0] for item in stat_pt_series]

  return render_template('dashboard.html',
                         home_jumlah=home_jumlah,
                         stat_prodi_keys=stat_prodi_keys,
                         stat_prodi_values=stat_prodi_values,
                         stat_pt_keys=stat_pt_keys,
                         stat_pt_values=stat_pt_values,
                         rerata_iku_keys=rerata_iku_keys,
                         rerata_iku_values=rerata_iku_values,
                         mhs_bidang_keys=mhs_bidang_keys,
                         mhs_bidang_values=mhs_bidang_values,
                         dsn_klmn_keys=dsn_klmn_keys,
                         dsn_klmn_values=dsn_klmn_values,
                         mhs_klmn_keys=mhs_klmn_keys,
                         mhs_klmn_values=mhs_klmn_values,
                         dsn_pt_keys=dsn_pt_keys,
                         dsn_pt_values=dsn_pt_values,
                         dsn_ik_keys=dsn_ik_keys,
                         dsn_ik_values=dsn_ik_values,
                         pen_mhs_keys=pen_mhs_keys,
                         pen_mhs_values=pen_mhs_values)


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
  #print('ridddddddd', college_list)
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
  return render_template(
    'detail-college.html',
    college_details=default_college_details,
    sum_details=None,
    stat_college=None,
    akreditasi_keys=None,
    akreditasi_values=None,
    dosen_value=None,
    mahasiswa_value=None,
    # latitude longitude
    latitude=None,
    longitude=None,
    # dosen tetap
    tetap_jumlah_jabatan_keys=None,
    tetap_jumlah_jabatan_values=None,
    tetap_jumlah_dosen_jenis_kelamin_keys=None,
    tetap_jumlah_dosen_jenis_kelamin_values=None,
    tetap_jumlah_jenjang_keys=None,
    tetap_jumlah_jenjang_values=None,
    tetap_jumlah_registrasi_keys=None,
    tetap_jumlah_registrasi_values=None,
    # dosen gk tetap
    tidak_tetap_jumlah_jabatan_keys=None,
    tidak_tetap_jumlah_jabatan_values=None,
    tidak_tetap_jumlah_dosen_jenis_kelamin_keys=None,
    tidak_tetap_jumlah_dosen_jenis_kelamin_values=None,
    tidak_tetap_jumlah_jenjang_keys=None,
    tidak_tetap_jumlah_jenjang_values=None,
    tidak_tetap_jumlah_registrasi_keys=None,
    tidak_tetap_jumlah_registrasi_values=None)


@app.route('/detail-college/<college_id>')
def detail_college_id(college_id):
  college = COLLEGE()
  # =================
  college_details = college.GetCollegeDetail(college_id)
  sp_details = college.GetSPDetail(college_id)
  sum_details = college.GetSumDetail(college_id)
  lc_detail = college.GetLecturerCollegeDetail(college_id)
  stat_college = college.StatisticCollege(college_id)
  # latitude and longitude
  latitude = college_details.get("lintang",
                                 0)  # Use the "lintang" value from the JSON
  longitude = college_details.get("bujur",
                                  0)  # Use the "bujur" value from the JSON
  # akreditasi jumlah
  akreditasi_keys = list(sum_details['jumlah_prodi_akreditasi'].keys())
  akreditasi_values = list(sum_details['jumlah_prodi_akreditasi'].values())
  # Extracting "dosen" and "mahasiswa" values from rasio_list
  dosen_value = sum_details['rasio_list'][0]['dosen']
  mahasiswa_value = sum_details['rasio_list'][0]['mahasiswa']
  # ================ dosen tetap =============================
  # dosen tetap jumlah jabatan
  tetap_jumlah_jabatan_series = lc_detail['tetap']['jumlah_dosen_jabatan'][
    'series']
  tetap_jumlah_jabatan_keys = [
    item['name'] for item in tetap_jumlah_jabatan_series
  ]
  tetap_jumlah_jabatan_values = [
    item['data'][0] for item in tetap_jumlah_jabatan_series
  ]
  # dosen tetap jumlah female dan male
  tetap_gender = lc_detail['tetap']
  tetap_jumlah_dosen_jenis_kelamin_keys = list(
    tetap_gender['jumlah_dosen_jenis_kelamin'].keys())
  tetap_jumlah_dosen_jenis_kelamin_values = list(
    tetap_gender['jumlah_dosen_jenis_kelamin'].values())
  # dosen tetap jenjang
  tetap_jumlah_jenjang_series = lc_detail['tetap']['jumlah_dosen_jenjang'][
    'series']
  tetap_jumlah_jenjang_keys = [
    item['name'] for item in tetap_jumlah_jenjang_series
  ]
  tetap_jumlah_jenjang_values = [
    item['data'][0] for item in tetap_jumlah_jenjang_series
  ]
  # jumlah dosen registrasi
  tetap_jumlah_registrasi_series = lc_detail['tetap'][
    'jumlah_dosen_registrasi']['series']
  tetap_jumlah_registrasi_keys = [
    item['name'] for item in tetap_jumlah_registrasi_series
  ]
  tetap_jumlah_registrasi_values = [
    item['data'][0] for item in tetap_jumlah_registrasi_series
  ]

  # ================ dosen non tetap =============================
  # dosen non tetap jumlah jabatan
  tidak_tetap_jumlah_jabatan_series = lc_detail['tidak_tetap'][
    'jumlah_dosen_jabatan']['series']
  tidak_tetap_jumlah_jabatan_keys = [
    item['name'] for item in tidak_tetap_jumlah_jabatan_series
  ]
  tidak_tetap_jumlah_jabatan_values = [
    item['data'][0] for item in tidak_tetap_jumlah_jabatan_series
  ]
  # dosen non tidak_tetap jumlah female dan male
  tidak_tetap_gender = lc_detail['tidak_tetap']
  tidak_tetap_jumlah_dosen_jenis_kelamin_keys = list(
    tidak_tetap_gender['jumlah_dosen_jenis_kelamin'].keys())
  tidak_tetap_jumlah_dosen_jenis_kelamin_values = list(
    tidak_tetap_gender['jumlah_dosen_jenis_kelamin'].values())
  # dosen non tidak_tetap jenjang
  tidak_tetap_jumlah_jenjang_series = lc_detail['tidak_tetap'][
    'jumlah_dosen_jenjang']['series']
  tidak_tetap_jumlah_jenjang_keys = [
    item['name'] for item in tidak_tetap_jumlah_jenjang_series
  ]
  tidak_tetap_jumlah_jenjang_values = [
    item['data'][0] for item in tidak_tetap_jumlah_jenjang_series
  ]
  # jumlah dosen non registrasi
  tidak_tetap_jumlah_registrasi_series = lc_detail['tidak_tetap'][
    'jumlah_dosen_registrasi']['series']
  tidak_tetap_jumlah_registrasi_keys = [
    item['name'] for item in tidak_tetap_jumlah_registrasi_series
  ]
  tidak_tetap_jumlah_registrasi_values = [
    item['data'][0] for item in tidak_tetap_jumlah_registrasi_series
  ]
  return render_template(
    "detail-college.html",
    college_id=college_id,
    college_details=college_details,
    sp_details=sp_details,
    sum_details=sum_details,
    akreditasi_keys=akreditasi_keys,
    akreditasi_values=akreditasi_values,
    dosen_value=dosen_value,
    mahasiswa_value=mahasiswa_value,
    # latitude longitude
    latitude=latitude,
    longitude=longitude,
    # dosen tetap
    tetap_jumlah_jabatan_keys=tetap_jumlah_jabatan_keys,
    tetap_jumlah_jabatan_values=tetap_jumlah_jabatan_values,
    tetap_jumlah_dosen_jenis_kelamin_keys=tetap_jumlah_dosen_jenis_kelamin_keys,
    tetap_jumlah_dosen_jenis_kelamin_values=
    tetap_jumlah_dosen_jenis_kelamin_values,
    tetap_jumlah_jenjang_keys=tetap_jumlah_jenjang_keys,
    tetap_jumlah_jenjang_values=tetap_jumlah_jenjang_values,
    tetap_jumlah_registrasi_keys=tetap_jumlah_registrasi_keys,
    tetap_jumlah_registrasi_values=tetap_jumlah_registrasi_values,
    # dosen gk tetap
    tidak_tetap_jumlah_jabatan_keys=tidak_tetap_jumlah_jabatan_keys,
    tidak_tetap_jumlah_jabatan_values=tidak_tetap_jumlah_jabatan_values,
    tidak_tetap_jumlah_dosen_jenis_kelamin_keys=
    tidak_tetap_jumlah_dosen_jenis_kelamin_keys,
    tidak_tetap_jumlah_dosen_jenis_kelamin_values=
    tidak_tetap_jumlah_dosen_jenis_kelamin_values,
    tidak_tetap_jumlah_jenjang_keys=tidak_tetap_jumlah_jenjang_keys,
    tidak_tetap_jumlah_jenjang_values=tidak_tetap_jumlah_jenjang_values,
    tidak_tetap_jumlah_registrasi_keys=tidak_tetap_jumlah_registrasi_keys,
    tidak_tetap_jumlah_registrasi_values=tidak_tetap_jumlah_registrasi_values,
    stat_college=stat_college)


# ================= STUDY PROGRAMS ===================
@app.route("/study-programs")
def study_programs():
  studyprograms = STUDY_PROGRAMS()
  studyprograms_list = studyprograms.StudyProgramsList()
  return render_template("study-programs.html",
                         studyprograms_list=studyprograms_list)


@app.route("/detail-sp")
def detail_sp():
  studyprogram_detail = {"detailumum": None}
  return render_template("detail-study-program.html",
                         studyprogram_detail=studyprogram_detail)


@app.route("/detail-sp/<sp_id>")
def detail_sp_id(sp_id):
  studyprograms = STUDY_PROGRAMS()
  studyprogram_detail = studyprograms.GetStudyProgramDetails(sp_id)

  # Extract latitude and longitude from the detailumum object
  latitude = studyprogram_detail["detailumum"]["lintang"]
  longitude = studyprogram_detail["detailumum"]["bujur"]
  # id college
  linkpt = studyprogram_detail["detailumum"]["linkpt"]
  linkpt_short = None  # Default value

  if linkpt is not None and "/data_pt/" in linkpt:
    linkpt_short = linkpt.split("/data_pt/")[1]

  return render_template("detail-study-program.html",
                         studyprogram_detail=studyprogram_detail,
                         latitude=latitude,
                         longitude=longitude,
                         linkpt_short=linkpt_short)


# ================= PROVINCES ========================
@app.route("/provinces")
def provinces():
  provinces = PROVINCES()
  provinces_list = provinces.ProvincesList()
  return render_template("provinces.html", provinces_list=provinces_list)
