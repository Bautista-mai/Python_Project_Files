for h in range(16, 0, -1):
    for e in range(1, h+1):
        print(" ",end=" ")
        
    for l in range(16, h, -1):
        print("*",end=" ")
        
    for o in range(15, h, -1):
        print("*",end=" ")
    print()
    
    
for h in range(1, 16):
    for e in range(1, h+2):
        print(" ",end=" ")
        
    for l in range(15, h, -1):
        print("*",end=" ")
        
    for o in range(14, h, -1):
        print("*",end=" ")
    print()        
        
