"""
E 
D E
C D E 
B C D E
A B C D E
"""

n = 5
base = 69

for row in range(1, n + 1):
  for col in range(1, row + 1):
    print(chr(base + col - row), end="    ")

  print("\n")
