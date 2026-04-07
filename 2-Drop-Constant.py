# Big 0: 0(n)

def print_items(n):
  for i in range(n):
    print(i)
  
  for j in range(n):
    print(j)

print_items(10)

# it is not 0(2n) because we drop the constant, so it is 0(n)