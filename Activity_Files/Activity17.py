def act17():
    for x in range(6, 0, -1):
        for z in range(1, x + 1):
            print(" ",end=" ")
        for y in range(6, x, -1):
            print("*",end=" ")
        for a in range(5, x, -1):
            print("*",end=" ")

        print()

    for x in range(1, 6):
        for z in range(1, x + 2):
            print(" ",end=" ")
        for y in range(5, x, -1):
            print("*",end=" ")
        for a in range(4, x, -1):
            print("*",end=" ")

        print()