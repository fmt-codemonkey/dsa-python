"""
A B C D E
A B C D
A B C
A B
A
"""

n = 5
base = 64

for row in range(n, 0, -1):
  for col in range(1, row + 1):
    print(chr(base + col), end="    ")
  print("\n")