"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* * 
*
"""

n = 5
for row in range(1, 2 * n + 1):
  star = row
  if (row > n):
    star = 2 * n - row

  for col in range(star):
    print("*", end="    ")
  print("\n")
