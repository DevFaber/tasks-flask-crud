class Task:
  def __init__(self, id, title, desc, completed=False) -> None:
    self.id = id,
    self.title = title,
    self.desc = desc,
    self.completed = completed,

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'desc': self.desc,
      'completed': self.completed
    }


