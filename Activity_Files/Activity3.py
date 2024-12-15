def Act3():
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

    print("\n\tGood day, My name is "+fullname+"!. I am "+gender+" and I'm currently ", age," years old. I was born on "+birthday+" in "+birthplace+". My parents name are "+f_name+" and "+m_name+". I am "+marital+" and I'm "+citizenship+" citizen, I belong to the "+religion+" religion and my weight and height are "+weight+" kg and "+height+" cm. I speak "+language+" languages. And my hobbies are "+hobbies+". I'm currently living in "+subd+","+street+","+brgy+","+city+","+province+" and you can contact me at", contact," or "+email+". Lastly, I'm currently a college student, I'm enrolled in DLL and my course is BSIT", bsit)
