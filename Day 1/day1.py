## for these, you can also use recursion to solve

def part1():
  ## opens txt file with depth values
  with open('inputDay1.txt', 'r') as f:
    d = f.readlines()
    inc = 0
    ## checks if depth increased between two readings
    for i, l in enumerate(d):
      if i == 0:
        p = int(l)
        continue
 
      if int(l) > p:
        inc += 1
      p = int(l)
 
    return inc

## essentially the same thing, just using 3 values instead of 1
def part2():
  ## this time used a list instead of just data
  with open('inputDay1.txt', 'r') as f:
    d = []
    for l in f:
      d.append(int(l.rstrip('\n')))
    inc = 0
    for i, l in enumerate(d):
    ## ends at last possible sum of 3 values
      if d[-3] is l:
        return inc
      s = l + d[i+1] + d[i+2]
      ns = d[i+1] + d[i+2] + d[i+3]
      if ns > s:
        inc += 1