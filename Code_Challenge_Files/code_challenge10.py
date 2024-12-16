#code_challenge10

def code10():

    for h in range(1, 16):
        for e in range(h,16):
            print(" ",end=" ")
            
        for l in range(1, h + 1):
            print("*",end=" ")
            
        for o in range(1, h + 1):
            print("*",end=" ")
        print()
        
        
        
    for h in range(1, 16):
        for e in range(1, h+1):
            print(" ",end=" ")
            
        for l in range(16, h, -1):
            print("*",end=" ")
            
        for o in range(16, h, -1):
            print("*",end=" ")
        print()        
            
    
  
