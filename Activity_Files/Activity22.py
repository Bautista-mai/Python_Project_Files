def act22():
    def act1():
        """Star"""
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* * * * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t*")
        
    def act2():
        """Flr Division"""
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        print(num1, "Floor Divided to", num2 , "=", num1 // num2)

    def act3():
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
        
    def act4():
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

    def act5():
        temp = int(input("Enter Temperature in Ferenheit: "))

        cel = (temp - 32) * 5/9
        round = (round(cel, 2))

        print(f" The convension of {temp} degrees farenheit is {round} degrees celcius. ")
    
    def act6():
        x = 5
        print(x)

        x += 10
        print(x)

        x += 15
        print(x)
        x += 30
        print(x)

    def act7():
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

    def act8():
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

    def act9():
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



        """Unfinished work"""