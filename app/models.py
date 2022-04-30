from re import I


class News_Source:
  '''
  News_Source class to define news objects
  '''

  def __init__(self, id, name, description, url):
      self.id = id
      self.name = name
      self.description = description
      self.url = url


class News:
  '''
  News class where news objects will be defined
  '''

  def __init__(self, source_name, title, author, description, url, image, date):
    self.source_name = source_name
    self.title = title
    self.author = author
    self.description = description
    self.url = url
    self.image = image
    self.date = date