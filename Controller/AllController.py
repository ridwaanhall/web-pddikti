import requests


class ReadUrl:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


class STUDENTS:

  def GetMhsList(self, search_name=None):  # Accept search_name parameter
    reader = ReadUrl()
    url = 'https://api-frontend.kemdikbud.go.id/hit_mhs/'
    if search_name:
      url += f"{search_name}"  # Modify the URL with the search_name parameter
    getmhs_list = reader.read_json(url)
    return getmhs_list


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
