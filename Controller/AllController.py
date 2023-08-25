import requests


class ReadUrl:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


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