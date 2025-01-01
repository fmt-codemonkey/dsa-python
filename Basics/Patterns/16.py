"""
A
B B
C C C
D D D D
E E E E E
"""

n = 5
base = 64
for row in range(1, n+ 1):
  for col in range(1, row + 1):
    print(chr(base + row), end="    ")
  print("\n")

