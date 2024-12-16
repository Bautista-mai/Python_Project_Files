def Act10():
    name = input("Enter your name: ")
    isstudent = input("Are you a student of DLL: ").upper().strip()

    if isstudent == "YES":
        yearlev = input("What year are you currently enrolled? \nf- Freshman \ns- Sophomore \nsn- senior: \n Please enter your grade level: ").upper().strip()

        if yearlev =="F":
            print(f"Hi your {name} , freshman, Welcome to DLL")

        elif yearlev == "S":
            print(f"Hi your {name} , sophomore, Welcome again to DLL")
            
        elif yearlev == "SN":
            print(f"Hi your {name} , senior, Welcome to DLL it's your last year. Goodluck!!")

    else:
        print("Thank you for using the system")
