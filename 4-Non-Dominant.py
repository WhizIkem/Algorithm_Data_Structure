# This is an example of a non-dominant term 
# the function below has 0(n^2) as dominant term and 0(n) as non-dominant term, so we drop the non-dominant term and the overall big O is 0(n^2)

def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i, j)

  for k in range(n):
    print(k)

print_items(10)