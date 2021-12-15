########################### PART 1 ###########################
def part1():
  draw, bb = getInfo()

## creates a draw order list and an array containing bingo boards and their rows
def getInfo():
  with open('inputDay4.txt', 'r') as f:
    draw = f.readline().rstrip("\n")
    bb = []
    rows = []
    ## creates 3d array containing each bingo board and row
    for i, l in enumerate(f):
      check = l.rstrip('\n').split()
      ## takes care of the empty lines
      if len(check) > 1:
        ## adds row to bingo board
        rows.append(check)
      ## adds bingo board to array
      if len(rows) == 5:
        bb.append(rows)
        rows = []
      if l == draw:
        pass
  ## have to split draw after loop because its needed to pass the first line
  draw = draw.split(',')

  return draw, bb