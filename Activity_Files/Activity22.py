def Act22():
    def Act1():
        """Star"""
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* * * * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t*")
        
    def Act2():
        """Flr Division"""
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        print(num1, "Floor Divided to", num2 , "=", num1 // num2)

    def Act3():
        """Bio Data"""
        print("\tPersonal Bio Data Registration:")


        fullname = input("What is your name: ")
        age = input("How old are you: ")
        gender = input("What is your gender: ")
        birthday = input("When is your birthday: ")
        birthplace = input("Where were you born: ")
        religion = input("What is your religion: ")
        f_name = input("What is your fathers name:")
        m_name = input("What is your mothers name: ")
        marital = input("What is your civil status: ")
        citizenship = input("what is your citizenship: ")
        language = input("What are the language you know: ")
        hobbies = input ("What is your hobbies: ")

        weight = input("What is your weight: ")
        height = input("What is your height: ")

        subd = input("What is the name of the subdivision your currently living: ")
        street = input("What is the name of the street: ")
        brgy = input("What is the name of the barangay: ")
        city = input("Enter Your City: ")
        province = input("What is your province: ")

        contact = input("What is your contact No.: ")
        email = input("What is your email adress: ")
        bsit = True

        print("\n\n\tPersonal Complete Bio Data:")

        print("\n\tGood day, My name is "+fullname+"!. I am "+gender+" and I'm currently ", age
              ," years old. I was born on "+birthday+" in "+birthplace+". My parents name are "+
              f_name+" and "+m_name+". I am "+marital+" and I'm "+citizenship+" citizen, I belong to the "+
              religion+" religion and my weight and height are "+weight+" kg and "+height+" cm. I speak "+
              language+" languages. And my hobbies are "+hobbies+". I'm currently living in "+subd+","+
              street+","+brgy+","+city+","+province+" and you can contact me at", contact," or "+email+
              ". Lastly, I'm currently a college student, I'm enrolled in DLL and my course is BSIT", bsit)
        
    def Act4():
        number1  = eval(input("enter a number --> "))

        number2 = eval(input("enter a number --> "))

        answer1 = number1 + number2
        answer2 = number1 - number2
        answer3 = number1 * number2
        answer4 = number1 / number2
        answer5 = number1 ** number2
        answer6 = number1 % number2
        answer7 = number1 // number2


        print("The sum of " , number1, " and " , number2, " is " , answer1)
        print("The difference of" , number1, " and " , number2, " is " , answer2)
        print("The product of" , number1, " and " , number2, " is " , answer3)
        print("The quotient of" , number1, " and " , number2, " is " , answer4)
        print("The exponent of" , number1, " and " , number2, " is " , answer5)
        print("The remainder of" , number1, " and " , number2, " is " , answer6)
        print("The floor division of" , number1, " and " , number2, " is " , answer7)

    def Act5():
        temp = int(input("Enter Temperature in Ferenheit: "))

        cel = (temp - 32) * 5/9
        round = (round(cel, 2))

        print(f" The convension of {temp} degrees farenheit is {round} degrees celcius. ")
    
    def Act6():
        x = 5
        print(x)

        x += 10
        print(x)

        x += 15
        print(x)
        x += 30
        print(x)

    def Act7():
        gold = 0
        min = input("Hi, What is your name: ")

        isgold = input("Is your mineral Gold? [Yes / No]: ").upper().strip()

        if isgold == "YES":
            gold += 1
            print(f"Hi {min}, Your total number of gold is: {gold}")

        elif isgold =="NO":
            print("Please input a gold")

        else:
            print("Invalid input")    

    def Act8():
        prelim = int(input("Prelim Score: "))
        mid = int(input("Midterm Score: "))
        semi = int(input("Semi-Final Score: "))
        final = int(input("Final Score: "))
        quiz = int(input("Quizes Score: "))
        proj = int(input('Project Score: '))

        ave = (prelim * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)
        print(f"Your grade is {ave}")

        if ave > 100:
            print("Error. Wrong Input")
        elif ave >= 65:
            print("You have passed")
        else:
            print("Sorry, You failed")

    def Act9():
        age = int(input("Enter your age: "))

        if age > 130:
            print("Enter your real age: ")
        elif age >= 60 and age <= 130:
            print("You are a senior")
        elif age >= 46 and age <= 59:
            print("You are at post adulthood")
        elif age >= 32 and age <= 45:
            print("You are at Mid Adulthood")
        elif age >= 19 and age <= 31:
            print("You are at Early Adulthood")
        elif age >= 14 and age <= 18:
            print("You are a teenager")
        elif age >= 8 and age <= 1:
            print("You are at pre - teen")
        elif age >= 1 and age <= 7:
            print("You are a todler")

        else:
            print("Invalid input")

    def Act10():
        name = input("Enter your name: ")
        isstudent = input("Are you a student of DLL: ").upper().strip()

        if isstudent == "YES":
            yearlev = input("What year are you currently enrolled? \nf- Freshman \ns- Sophomore \nsn- senior: \n Please enter your grade level: ").upper().strip()

            if yearlev =="f":
                print(f"Hi your {name} , freshman, Welcome to DLL")

            elif yearlev == "s":
                print(f"Hi your {name} , sophomore, Welcome again to DLL")
                
            elif yearlev == "sn":
                print(f"Hi your {name} , senior, Welcome to DLL it's your last year. Goodluck!!")

        else:
            print("Thank you for using the system")

    def Act11():
        for i in range(89):
            print("Codieeee")
            print("Keep going")
            
            cute = False
            print(f"{cute}, that I'm cute")

    def Act12():
        for i in range(10, 1, -1):
            print(i)

    def Act13():
        sum = 0
        for i in range(6, 0, -1):
            i *= i
            sum += i

        print(i)
        print(sum)         

    def Act14():
        for i in range(0, 11):
            print(i,end="")
            for a in range(0,11):
                print("*",end=(" "))
            print()

    def Act15():
        for i in range(0,11):
            print(i,end=" ")
            for a in range(0,i):
                print("*",end=(" "))
            print()

    def Act16():
        for x in range(1, 11):
            for z in range(1, x + 1):
                print(" ",end=" ")
            for y in range(11, x, -1):
                print("*",end=" ")

            print()
        
    def Act17():
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
    
    def Act18():
        num = int(input("Enter a number of right tringle: "))

        for i in range(1, 6):
            for y in range(1, num + 1):
                print(" ",end=" ")
                for u in range(1, i + 1):
                    print("*",end=" ")
                for n in range(5,i, -1):
                    print(" ",end=" ")

            print()

    def Act19():
        isContinue = True

        while isContinue:
            name = input("Give me name: ")

            if name.lower() == "stop":
                print("Loop terminated")
                break

                isContinue = False
            else:
                print(f"Hi {name}")
                continue

    def Act20():
        continu = True
        count = 0

        while continu == True:
            name = input("Enter a name: ").uppr().strip()

            if name == "STOP":
                print("The loop has now atopped")
                print(f"You have entered {count} number of names")
                break

            else:
                count += 1
                continue

    def Act21():
        def cute():
            print("Hello, you're cute")

        def tri():
            num = int(input("Enter a number of right tringle: "))
            for i in range(1, 6):
                for y in range(1, num + 1):
                    print(" ",end=" ")
                    for u in range(1, i + 1):
                        print("*",end=" ")
                    for n in range(5,i, -1):
                        print(" ",end=" ")
            print()

        cute()
        tri()

    def Act23():
        def add(num1, num2):
            """This function adds the first number and second number returnig sum value"""
            return print(f"The sum of the numbers are ---> {num1 + num2}")    
        
        add(1, 2)

    def Act24():
        from Activity23 import Act23
        import Activity1 

        Act23()
        Activity1

    def Act25():
        courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

        courses.remove("Delete w/o index")
        courses.pop()
        courses.append("DHRS")
        courses.insert(0, "ABELS")

        print(courses)

    while True:
            try:

                print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                    "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]"
                    "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]"
                    "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]"
                    "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]"
                    "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [23]"
                    "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [24]"
                    "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [25]"
                    "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", "\tExit - [0]")

                num = int(input("\n\n\tSelect a Program: "))

                if num == 1:
                    Act1()
                    continue

                elif num == 2:
                    Act2()
                    continue

                elif num == 3:
                    Act3()
                    continue

                elif num == 4:
                    Act4()
                    continue

                elif num == 5:
                    Act5()
                    continue

                elif num == 6:
                    Act6()
                    continue
                
                elif num == 7:
                    Act7()
                    continue

                elif num == 8:
                    Act8()
                    continue

                elif num == 9:
                    Act9()
                    continue

                elif num == 10:
                    Act10()
                    continue

                elif num == 11:
                    Act11()
                    continue

                elif num == 12:
                    Act12()
                    continue

                elif num == 13:
                    Act13()
                    continue

                elif num == 14:
                    Act14()
                    continue
                    
                elif num == 15:
                    Act14()
                    continue

                elif num == 16:
                    Act16()
                    continue

                elif num == 17:
                    Act17()
                    continue
                
                elif num == 18:
                    Act18()
                    continue

                elif num == 19:
                    Act19()
                    continue

                elif num == 20:
                    Act20()
                    continue

                elif num == 21:
                    Act21()
                    continue

                elif num == 23:
                    Act23()
                    continue

                elif num == 24:
                    Act24()
                    continue

                elif num == 25:
                    Act25()
                    continue
                
                elif num == 0:
                    cont = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                    if cont == "YES":
                            print("The program will not be terminated")
                            print("Thank you for using the program")
                            break

                    elif cont == "NO":
                            print("The program will now continue")
                            continue

                    else:
                            print("Wrong Input. Invalid Answer")


                elif num < 0:
                    print("Wrong Input. Must Be A Positive Number.")
                    continue

                else:
                    print("Wrong Input. Invalid Answer")
                    continue

            except ValueError:
                print("Wrong Input. Must Be A Number.")
                continue
