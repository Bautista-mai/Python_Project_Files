#codechalleng13

i = 0

for h in range(1, 9 ):
    for e in range(8 - i): 
        print(" ", end=" ")
        
    for i in range(h, 0, -1): 
        print(i, end=" ")
        
    for i in range(2, h + 1): 
        print(i, end=" ")

    print()

for i in range(9, 0, -1):
    for s in range(9, i, - 1):
        print(" ", end= " ")
        
    for o in range(i, 1, - 1):
        print(o, end= " ")
        
    for t in range(1, i + 1):
        print(t, end= " ")
    print()