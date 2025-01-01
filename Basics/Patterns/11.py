"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

n = 5
for row in range(1, n + 1):
  start = 1
  if row % 2 == 0: 
    start = 0

  for col in range(row):
    print(start, end="    ")
    start = 1 - start
  
  print("\n")