import requests


class ReadUrl:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


class STUDENTS:

  def GetMhsList(self, search_name=None):
    reader = ReadUrl()
    url = 'https://api-frontend.kemdikbud.go.id/hit_mhs/'
    if search_name:
      url += f"{search_name}"
    getmhs_list = reader.read_json(url)

    if getmhs_list is None:
      return []

    if "Cari kata kunci" in getmhs_list.get("mahasiswa", [])[0]["text"]:
      return [{"text": getmhs_list["mahasiswa"][0]["text"]}]

    filtered_students = []
    for student in getmhs_list.get("mahasiswa", []):
      if search_name and search_name.lower() not in student["text"].lower():
        continue
      info = student["text"].split(", ")
      name = info[0].split("(")[0]
      id_number = info[0].split("(")[1].split(")")[0]
      college = info[1].split(" : ")[1]
      program = info[2].split(": ")[1]
      link = student["website-link"]
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
