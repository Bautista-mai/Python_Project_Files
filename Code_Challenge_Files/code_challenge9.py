#codechallenge9

def code9():
    for i in range(1, 10):
        for m in range(1, i+1):
            print(" ",end=" ")

        for a in range(10, i, -1):
            print("*",end= " ")
        print()    

