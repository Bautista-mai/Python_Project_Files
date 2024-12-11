import os
trut = True
num = 0
while trut == True:
    tatsu = input("Would you like to add a triangle?(Yes/No): ")
    
    if tatsu.lower() == "no":
        os.system('cls')
        print("Program terminatted. Please try again Later")
        break
        
    elif tatsu.lower() == "yes":
        os.system('cls')
        num += 1
        for x in range(1,6):
            for r in range(1, num+1):
                for y in range(1,x+1):
                    print("*", end=" ")
                for z in range (6,x,-1):
                    print("  ",end="")
            print()
        continue
        
    else:
        os.system('cls')
        print("Answer is not valid. Please input only yes or no")
        continue