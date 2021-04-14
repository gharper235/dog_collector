class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'foul little demon', 3),
  Dog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Dog('Raven', 'black tripod', '3 legged cat', 4)
]