"""
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""

n = 5
space_number = 2 * n - 2
for row in range(1, 2 * n):
  star_number = row
  if row > n:
    star_number = 2 * n - row

  # star 
  for star in range(star_number):
    print("*", end="    ") 

  # space
  for space in range(space_number):
    print(" ", end="    ") 

  # star 
  for star in range(star_number):
    print("*", end="    ") 
  
  if row < n: 
    space_number -= 2
  else: 
    space_number += 2

  print("\n")