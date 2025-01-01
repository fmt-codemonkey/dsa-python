"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""

n = 4
space_ = 2 * (n - 1)
for row in range(1, n + 1):
  # number
  for col in range(1, row+ 1):
    print(col, end="    ")

  # space 
  for space in range(space_):
    print(" ", end="    ")

  # number 
  for col in range(row, 0, -1):
    print(col, end="    ")
  print("\n")
  space_ -= 2