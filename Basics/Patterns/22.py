"""
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""

n = 4
outer_loop = 2 * n - 1
inner_loop = 2 * n - 1

for row in range(outer_loop):
  for col in range(inner_loop):
    top = row
    left = col 
    right = ( 2 * n - 1) - 1 - col
    bottom = ( 2 * n - 1) - 1 - row

    print((n - min(min(top, bottom), min(left, right))), end="    ")
  print("\n")