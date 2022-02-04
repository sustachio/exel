# this will not be there, the errors were just getting annoying
class Section():
  def __init__(self, start, end) -> None:
      pass

mainArea = Section( 
  start="A2", 
  end  ="N12"
)

# the top left cell of main-area
variable = mainArea.cell("A1")

# change the value of a cell
variable.val("this is a cell")

# these will both get the cells in a column
column = mainArea.column("B")
column = mainArea.column("2")

for i, cell in enumerate(column):
  cell.val(i)