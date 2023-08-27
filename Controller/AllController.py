import requests
from urllib.parse import quote


class ReadUrl:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


class STUDENTS:

  def GetStudentDetail(self, student_id):
    reader = ReadUrl()
    detail_url = f'https://api-frontend.kemdikbud.go.id/detail_mhs/{student_id}'
    student_details = reader.read_json(detail_url)
    return student_details

  def GetMhsList(self, search_name=None):
    reader = ReadUrl()
    url = 'https://api-frontend.kemdikbud.go.id/hit_mhs/'
    if search_name:
      encoded_search_name = quote(search_name)
      url += encoded_search_name
    #print('iniiiii url ', url)
    getmhs_list = reader.read_json(url)
    #print("hhe list mhs", getmhs_list)
    if getmhs_list is None:
      return []

    if "Cari kata kunci" in getmhs_list.get("mahasiswa", [])[0]["text"]:
      return [{"text": getmhs_list["mahasiswa"][0]["text"]}]

    filtered_students = []
    for student in getmhs_list.get("mahasiswa", []):
      # this for more specify
      #if search_name and search_name.lower() not in student["text"].lower():
      #  continue
      info = student["text"].split(", ")
      name = info[0].split("(")[0]
      id_number = info[0].split("(")[1].split(")")[0]
      college = info[1].split(" : ")[1]
      program = info[2].split(": ")[1]
      link = student["website-link"]
      link = link.replace("/data_mahasiswa", "")
      filtered_students.append({
        "name": name,
        "id_number": id_number,
        "college": college,
        "program": program,
        "website-link": link
      })

    return filtered_students


class COLLEGE:

  def CollegeList(self):
    reader = ReadUrl()
    college_list = reader.read_json(
      'https://api-frontend.kemdikbud.go.id/loadpt')
    return college_list


class STUDY_PROGRAMS:

  def StudyProgramsList(self):
    reader = ReadUrl()
    studyprograms_list = reader.read_json(
      'https://api-frontend.kemdikbud.go.id/loadprodi')
    return studyprograms_list


class PROVINCES:

  def ProvincesList(self):
    reader = ReadUrl()
    provinces_list = reader.read_json(
      'https://api-frontend.kemdikbud.go.id/get_provinsi')
    return provinces_list


class SEARCH_OTHER:
  url_base = 'https://api-frontend.kemdikbud.go.id/hit/'

  def GetDsnList(self, search_name=None):
    reader = ReadUrl()
    url = self.url_base
    if search_name:
      encoded_search_name = quote(search_name)
      url += encoded_search_name
    getdsn_list = reader.read_json(url)
    #print("list dosen", getdsn_list)
    if getdsn_list is None:
      return []

    if "Cari kata kunci" in getdsn_list.get("dosen", [])[0]["text"]:
      return [{"text": getdsn_list["dosen"][0]["text"]}]

    filtered_dosens = []
    for dosen in getdsn_list.get("dosen", []):
      info = dosen["text"].split(", ")
      name = info[0]
      nidn = info[1].split(": ")[1]
      college = info[2].split(": ")[1]
      program = info[3].split(": ")[1]
      link = dosen["website-link"].replace("/data_dosen", "")

      filtered_dosens.append({
        "name": name,
        "nidn": nidn,
        "college": college,
        "program": program,
        "website-link": link
      })
    #print('filterrrr', filtered_dosens)
    return filtered_dosens

  def GetProdiList(self, search_name=None):
    reader = ReadUrl()
    url = self.url_base
    if search_name:
      encoded_search_name = quote(search_name)
      url += encoded_search_name
    getprodi_list = reader.read_json(url)
    #print("list prodi", getprodi_list)
    if getprodi_list is None:
      return []

    if "Cari kata kunci" in getprodi_list.get("prodi", [])[0]["text"]:
      return [{"text": getprodi_list["prodi"][0]["text"]}]

    filtered_prodis = []
    for prodi in getprodi_list.get("prodi", []):
      info = prodi["text"].split(", ")
      program = info[0].split(": ")[1]
      level = info[1].split(": ")[1]
      college = info[2].split(": ")[1]
      link = prodi["website-link"].replace("/data_prodi", "")

      filtered_prodis.append({
        "program": program,
        "level": level,
        "college": college,
        "website-link": link
      })
    return filtered_prodis

  def GetPTList(self, search_name=None):
    reader = ReadUrl()
    url = self.url_base
    if search_name:
      encoded_search_name = quote(search_name)
      url += encoded_search_name
    getpt_list = reader.read_json(url)
    #print("list prodi", getpt_list)
    if getpt_list is None:
      return []

    if "Cari kata kunci" in getpt_list.get("pt", [])[0]["text"]:
      return [{"text": getpt_list["pt"][0]["text"]}]

    filtered_pts = []
    for pt in getpt_list.get("pt", []):
      info = pt["text"].split(", ")
      college = info[0].split(": ")[1]
      npsn = info[1].split(": ")[1].strip()
      abbreviation = info[2].split(": ")[1]
      address = " ".join(info[3].split(": ")[1:])

      link = pt["website-link"].replace("/data_pt", "")

      filtered_pts.append({
        "college": college,
        "npsn": npsn,
        "abbreviation": abbreviation,
        "address": address,
        "website-link": link
      })
    return filtered_pts
