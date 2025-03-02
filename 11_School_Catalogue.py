class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
#getters
  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents
#setters
  def setName(self, name):
    self.name = name

  def setLevel(self, level):
    self.level  = level

  def setNumberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students' 

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getpickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self): 
    return super().__repr__( ) + f" Pickup policy: {self.pickupPolicy}."

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def getsportsTeams(self):
    return self.sportsTeams  

  def __repr__(self): 
    return super().__repr__( ) + f" Sports Team: {', '.join(self.sportsTeams)}."  

#testcases

school = School("Codecademy", "high", 100)
print(school)
print(school.getName())
print(school.getLevel())
school.setNumberOfStudents(200)
print(school.getNumberOfStudents())
 
#primary
primary = PrimarySchool("Codeacademy", 100, "Pickup after 3pm")
print(primary)
print(primary.getName())
print(primary.getLevel())
primary.setNumberOfStudents(200)
print(primary.getNumberOfStudents())

#highSchool
highschool = HighSchool("Codeacademy", 100, ["Arsenal", "ManU", "Chelsea"])
print(highschool)
print(highschool.getName())
print(highschool.getLevel())
highschool.setNumberOfStudents(200)
print(highschool.getNumberOfStudents())
    
