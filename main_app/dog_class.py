class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Phoebe', 'Boston Terrier', 'devious tongue-demon', 3),
  Dog('Lucy', 'Boston Mix', 'the original sweet lick', 7),
  Dog('Champ', 'Golden Retriever', 'childhood friend', 0)
]