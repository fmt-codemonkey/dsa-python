"""
      A
    A B A
  A B C B A
A B C D C B A
"""

n = 4
base = 64
for row in range(1, n+ 1):
  # space 
  for space in range(n-row):
    print("", end="    ")
  # character 
  for char in range(1, 2 * row):
    if char < row:
      print(chr(base + char), end="    ")
    else:
      print(chr(base + 2 * row - char), end="    ")
  # space 
  for space in range(n-row):
    print("", end="    ")

  print("\n")