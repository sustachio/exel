"""
todo:

-line 51
"""



# one type of variable
class String():
  def __init__(self, value):
    self.value = value

# each variable will be one of these
class Variable():
  def __init__(self, name, value, _type):
    self.name = name
    self.type = _type
    
    if _type == "string":
      self.content = String(value)
    
  # return value if it is being printed
  def __repr__(self):
    return(f"VARIABLE OBJ: NAME [{self.name}] VALUE [{self.content.value}] TYPE [{self.type}]")


# this will be the compiler class that basicially does everything
class Compiler():
  def __init__(self):
    # get all lines in the file
    with open("Super SpreadSheet Script/bestprogramminglanguage.ssss", "r") as f:
      self.file = [i for i in f.read().split("\n")]
      print(self.file)


  # look for errors in the file before compiling
  def checker(self):
    
    # list of created variables so you cant read from a variable if it hasent been created
    foundVariables = []
    
    # loop through the lines in the file
    for line in self.file:
      # check for new variable and append the name to foundVariables
      if "+$" in line:
        foundVariables.append(line.split("=")[0].strip("+$\t "))
        
      # if a variable is being called
      elif "$" in line:
        # check if the variable is in foundVariables
        pass
        
        
    print(foundVariables)
      
compiler = Compiler()
compiler.checker()