def part1():
  g = gamma()
  e = toDec(epsilon(g))
  g = toDec(g)

  return g*e

## counts the number of 1 and 0 bits at index n and adds most common to g
def gamma():
  with open('inputDay3.txt', 'r') as f:
    d = []
    for l in f:
      d.append(l.rstrip('\n'))
    g = ''
    for n in range(0, 12):
      count1 = 0
      count0 = 0
      for c in d:
        if c[n] == '1':
          count1 += 1
        else: 
          count0 += 1
      if count1 > count0:
        g += '1'
      else:
        g += '0'

  return g

## changes each bit from most common to least common
def epsilon(g):
  e = ''
  for c in g:
    if c == '1':
      e += '0'
    else:
      e += '1'
  
  return e

## converts from binary to decimal
def toDec(binary):
  decimal = 0
  for digit in binary:
    decimal = decimal*2 + int(digit)

  return decimal