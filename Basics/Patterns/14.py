"""
A
A B
A B C
A B C D
A B C D E
"""

n = 5
base = 64

for row in range(1, n + 1):
  for col in range(1, row + 1):
    print(chr(base + col), end="    ")
  print("\n")