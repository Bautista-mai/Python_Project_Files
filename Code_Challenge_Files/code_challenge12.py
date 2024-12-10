#code challenge12
  
for h in range(1, 10):
  for e in range(h, 10):
    print(" ",end=" ")
  for l in range(2, h + 1):
    print("*", end=" ")
  for o in range(2,h + 1):
    print("*", end=" ")
  print()

for k in range(1,9):
  for i in range(2,h - 4):
    print("    ",end=" ")
  for t in range(2, h - 4):
    print("*", end=" ")
  print()
  
  