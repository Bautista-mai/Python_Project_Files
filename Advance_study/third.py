#hospital
while  True:
    name = input("\nEnter your name: ")
    patient = input("\n Are you a patient?: ").upper().strip()


    if patient == "YES":
        new = input("\nEnter if you are old or new patient: ").upper().strip()
        
        if new == "NEW":
            print(f"Welcome {name} to doctors hospital")

        elif new == "OLD":
            print(f"We're glad to serve you again {name}")

    else:
        print("Have a good day!")
        break





    # name = input("\nEnter your name: ").upper().strip()
    # age = (input("\nEnter your age: "))
    # patient = input("\nEnter old or new patient: ").upper().strip()


    # if name == "JOHN SMITH":
    #     print(age)

    #     if age == 20:
    #         print(patient)

    #     if patient == "NEW":
    #         print("\nPatient found")

    # elif name == 

    # else:
    #     print("\n Thank you for using. You're not the missing patient")
    #     continue
        

