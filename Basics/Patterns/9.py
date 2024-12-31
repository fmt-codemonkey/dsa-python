"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
* * * * * * * * *
  * * * * * * *
    * * * * * 
      * * * 
        *
"""
# upper part 
n = 5
for row in range(1, n + 1):
  # space 
  for space in range(n - row):
    print("", end=" ")
  # star 
  for start in range(2 * row - 1):
    print("*", end="")

  # space 
  for space in range(n-row):
    print("", end=" ")
  
  print("\n")

# lower part 
n = 5
for row in range(1, n + 1):
  # space 
  for space in range(row - 1):
    print("", end=" ")
  # star 
  for star in range(2 * n - (2 * row - 1)):
    print("*", end="")
  # space 
  for space in range(row - 1):
    print("", end=" ")
  print("\n")