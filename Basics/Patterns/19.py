"""
* * * * * * * * * *
* * * *     * * * *
* * *         * * * 
* *             * * 
*                 *
*                 *
* *             * *
* * *         * * * 
* * * *     * * * *            
* * * * * * * * * *
"""

n = 5

# upper part 
spaces = 0 
for row in range(1, n + 1):
  # star 
  for col in range(n - row + 1):
    print("*", end="    ") 
  # space 
  for space in range(spaces):
    print(" ", end="    ")

  spaces += 2
  # star 
  for col in range(n + 1 - row):
    print("*", end="    ") 

  print("\n")

  # lower part 
  spaces_ = 2 * n - 2 
for row_ in range(1, n + 1):
  # star 
  for col_ in range(row_):
    print("*", end="    ") 
  # space 
  for space_ in range(spaces_):
    print(" ", end="    ")

  spaces_ -= 2
  # star 
  for col_ in range(row_):
    print("*", end="    ") 

  print("\n")
