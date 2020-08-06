# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.items = [items]
  
  def __str__(self):
    return f"""\nName: {self.name}\nDescription: {self.description}\nItems: {self.items}\n"""

  def remove_item(self, item):
    del self.items[item]
  
  def add_item(self, item):
    self.items.append(item)
