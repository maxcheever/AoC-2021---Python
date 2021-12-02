def part1():
  with open("inputDay2.txt", "r") as f:
    d = f.readlines()
    h = 0 
    v = 0
    ## makes a list with each direction, number value
    for l in d:
      newL = l.rstrip("\n").split()
      newL[1] = int(newL[1])
      ## adds to depth or height according to direction value
      if newL[0] == 'forward':
        h += newL[1]
      if newL[0] == 'down':
        v += newL[1]
      if newL[0] == 'up':
        v -= newL[1]
  mult = h*v
  return mult

def part2():
  with open("inputDay2.txt", "r") as f:
    d = f.readlines()
    h = 0 
    ## this time needs to have an aim value
    a = 0
    v = 0
    for l in d:
      newL = l.rstrip("\n").split()
      newL[1] = int(newL[1])
      if newL[0] == 'forward':
        h += newL[1]
        ## the 'forward' value is now what changes the depth
        if a > 0:
          v += (newL[1]*a)
      ## now the 'up' and 'down' directions change the value of aim instead of depth
      if newL[0] == 'down':
        a += newL[1]
      if newL[0] == 'up':
        a -= newL[1]
  mult = h*v
  return mult