######################### PART 1 ###########################
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


######################### PART 2 ###########################
def part2():
  d = getReadings()
  carbon = toDec(cScrub(d))
  oxygen = toDec(oRate(d))
  final = oxygen*carbon
  
  return final

## gets all readings and returns a list of them
def getReadings():
  with open('inputDay3.txt', 'r') as f:
    d = []
    for l in f:
      d.append(l.rstrip('\n'))
  
  return d

## counter for the most common bit at a given index
def counter(d, i):
  count1 = 0
  count0 = 0
  for v in d:
    if v[i] == '0':
      count0 += 1
    else:
      count1 += 1
  if count1 > count0 or count1 == count0:
    return '1'
  else:
    return '0'

## finds the oxygen scrubber rate in binary
def oRate(d):
  oBin = d
  for i in range(0,12):
    newBin = []
    ## finds most common bit
    most = counter(oBin,i)
    ## appends every value with most common bit at index i
    if most == '1':
      for v in oBin:
        if v[i] == '1':
          newBin.append(v)
      ## the new list only will contain values with most common occurence
      oBin = newBin
    ## same idea here, just if 0 is most common occurence
    else:
      for v in oBin:
        if v[i] == '0':
          newBin.append(v)
      oBin = newBin

  return oBin[0]

## this is the same as the oxygen scrubber rate, just with least common bit
def cScrub(d):
  cBin = d
  for i in range(0,12):
    newBin = []
    most = counter(cBin,i)
    if most == '1':
      for v in cBin:
        if v[i] == '0':
          newBin.append(v)
      cBin = newBin
    else:
      for v in cBin:
        if v[i] == '1':
          newBin.append(v)
      cBin = newBin
    if len(cBin) == 1:
      break

  return cBin[0]