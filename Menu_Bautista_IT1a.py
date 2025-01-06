import os

from Activity_Files import ( 

                    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7,
                    Activity8, Activity9, Activity10, Activity11, Activity12, Activity13, Activity14,
                    Activity15, Activity16, Activity17, Activity18, Activity19, Activity20, Activity21,
                    Activity22, Activity23, Activity24, Activity25

                    )

from Code_Challenge_Files import (

                    Code_Challenge1, Code_Challenge2, Code_Challenge3, Code_Challenge4, Code_Challenge5,
                    Code_Challenge6, Code_Challenge7, Code_Challenge8, Code_Challenge9, Code_Challenge10,
                    Code_Challenge11, Code_Challenge12, Code_Challenge13, Code_Challenge14, Code_Challenge15,
                    Code_Challenge16    

                    )

def Acts():
        while True:
            try:
                print("\nCOMPILATION OF PROJECTS\n"
                        "--------------------------\n"
                        "---------> MENU <---------\n"
                
                
                        "\n1 - Activities Compilations\n"
                        "2 - Code_challenge_Compilations\n"
                        "3 - Python Fundamentals\n"
                        "0 - Terminate\n"
                
                "======================================="
                
                "\n\n\t 1  - Activity_1  \t 14  - Activity_14"
                    "\n\t 2  - Activity_2  \t 15  - Activity_15"
                    "\n\t 3  - Activity_3  \t 16  - Activity_16"
                    "\n\t 4  - Activity_4  \t 17  - Activity_17"
                    "\n\t 5  - Activity_5  \t 18  - Activity_18"
                    "\n\t 6  - Activity_6  \t 19  - Activity_19"
                    "\n\t 7  - Activity_7  \t 20  - Activity_20"
                    "\n\t 8  - Activity_8  \t 21  - Activity_21"
                    "\n\t 9  - Activity_9  \t 22  - Activity_22"
                    "\n\t 10  - Activity_10  \t 23  - Activity_23"
                    "\n\t 11  - Activity_11  \t 24  - Activity_24"
                    "\n\t 12  - Activity_12  \t 25  - Activity_25"
                    "\n\t 13  - Activity_13  \t 0  - Terminate\n"
                    
                    )
            
                cho = int(input("Choose A Number: "))

                if cho == 1:
                    Activity1.Act1()
                elif cho == 2:
                    Activity2.Act2()
                elif cho == 3:
                    Activity3.Act3()
                elif cho == 4:
                    Activity4.Act4()
                elif cho == 5:
                    Activity5.Act5()
                elif cho == 6:
                    Activity6.Act6()
                elif cho == 7:
                    Activity7.Act7()
                elif cho == 8:
                    Activity8.Act8()
                elif cho == 9:
                    Activity9.Act9()
                elif cho == 10:
                    Activity10.Act10()
                elif cho == 11:
                    Activity11.Act11()
                elif cho == 12:
                    Activity12.Act12()
                elif cho == 13:
                    Activity13.Act13()
                elif cho == 14:
                    Activity14.Act14()
                elif cho == 15:
                    Activity15.Act15()
                elif cho == 16:
                    Activity16.Act16()
                elif cho == 17:
                    Activity17.Act17()
                elif cho == 18:
                    Activity18.Act18()
                elif cho == 19:
                    Activity19.Act19()
                elif cho == 20:
                    Activity20.Act20()
                elif cho == 21:
                    Activity21.Act21()
                elif cho == 22:
                    Activity22.Act22()
                elif cho == 23:
                    Activity23.Act23()
                elif cho == 24:
                    Activity24.Act24()
                elif cho == 25:
                    Activity25.Act25()

                elif cho == 0:
                    print("This Activities  be terminated")
                    sur = input("Are you sure? (Yes/No): ").strip().lower()
                            
                    if sur == "yes":
                        delete()
                        print("The Activities will finally terminated.")
                        break

                    elif sur == "no":
                        delete()
                        print("The Activities will still continue.")
                        continue

                    else:
                        print("Invalid Input.")

                elif cho < 0:
                    print("Error. Enter A Positive Number.")
                elif cho >= 26:
                    print("Error.  Enter A number from the choices.")
                else:
                    print("Invalid input.")
            
            except ValueError:
                print("\nInvalid, Please enter from the choices only.")
                continue
        
def codes():
    while True:
        try:
            print("\nCOMPILATION OF PROJECTS\n"
                        "--------------------------\n"
                        "---------> MENU <---------\n"
                
                
                        "\n1 - Activities Compilations\n"
                        "2 - Code_challenge_Compilations\n"
                        "3 - Python Fundamentals\n"
                        "0 - Terminate\n\n "

                "======================================="
                            
                "\n\n\t 1  - Code_Challenge1"
                    "\n\t 2  - Code_Challenge2"
                    "\n\t 3  - Code_Challenge3"
                    "\n\t 4  - Code_Challenge4"
                    "\n\t 5  - Code_Challenge5"
                    "\n\t 6  - Code_Challenge6"
                    "\n\t 7  - Code_Challenge7"
                    "\n\t 8  - Code_Challenge8"
                    "\n\t 9  - Code_Challenge9"
                    "\n\t 10 - Code_Challenge10"
                    "\n\t 11 - Code_Challenge11"
                    "\n\t 12 - Code_Challenge12"
                    "\n\t 13 - Code_Challenge13"
                    "\n\t 14 - Code_Challenge14"
                    "\n\t 15 - Code_Challenge15"
                    "\n\t 16  - Code_Challenge16"
                    "\n\t 0 - Terminated\n"
                    
                    )

            choi = int(input("Choose a Number: "))
        
            if choi ==  1:
                Code_Challenge1.code1()
            elif choi == 2:
                Code_Challenge2.code2()
            elif choi == 3:
                Code_Challenge3.code3()
            elif choi == 4:
                Code_Challenge4.code4()
            elif choi == 5:
                Code_Challenge5.code5()
            elif choi == 6:
                Code_Challenge6.code6()
            elif choi == 7:
                Code_Challenge7.code7()
            elif choi == 8:
                Code_Challenge8.code8()
            elif choi == 9:
                Code_Challenge9.code9()
            elif choi == 10:
                Code_Challenge10.code10()
            elif choi == 11:
                Code_Challenge11.code11()
            elif choi == 12:
                Code_Challenge12.code12()
            elif choi == 13:
                Code_Challenge13.code13()
            elif choi == 14:
                Code_Challenge14.code14()
            elif choi == 15:
                Code_Challenge15.code15()
            elif choi == 16:
                Code_Challenge16.code16()
        
            elif choi == 0:
                    print("This Activities  be terminated.")

                    sur = input("Are you sure? (Yes/No): ").strip().lower()          
                    if sur == "yes":
                        delete()
                        print("The Activities will finally terminated.")
                        break

                    elif sur == "no":
                        delete()
                        print("The Activities will still continue.")
                        continue

                    else:
                        print("Invalid Input.")

            elif choi < 0:
                print("Error. Enter A Positive Number.")
            elif choi >= 17:
                print("Error.  Enter A number from the choices.")
            else:
                print("Invalid input.")
        
        except ValueError:
                print("\nInvalid, Please enter from the choices only.")
                continue


def delete():
    os.system("cls")

def menu():
    while True:
        try:
            print("\n-> COMPILATION OF PROJECTS <-\n"
                "------------------------------\n"
                "-----------> MENU <-----------\n"
                
                
                "\n1 - Activities Compilations\n"
                "2 - Code challenge Compilations\n"
                "3 - Python Fundamentals\n"
                "0 - Terminate\n"
                
                )
            
            choose = int(input("Choose A number: "))

            if choose == 1:
                    Acts()
            elif choose == 2:
                    codes()
            elif choose == 3:
                    funda()
            elif choose == 0:
                print("This Activities  be terminated.")

                sur = input("Are you sure? (Yes/No): ").strip().lower()       
                if sur == "yes":
                    delete()
                    print("The Activities will finally terminated.")
                    break

                elif sur == "no":
                    delete()
                    print("The Activities will still continue.")
                    continue

                else:
                        print("Invalid Input")

            elif choose < 0:
                print("Error. Enter A Positive Number.")
            elif choose >= 26:
                print("Error.  Enter A number from the choices.")
            else:
                print("Invalid input.")
        except ValueError:
                print("\nInvalid input, Please enter from the choices only.")
                continue

def funda():
    while True:
        try:
            print("\n-----COMPILATION OF PROJECTS------\n"
                        "---------------------------------\n"
                        "---------> FUNDAMENTALS <---------\n"
            
                        "\n1 - Activities Compilations\n"
                        "2 - Code_challenge_Compilations\n"
                        "3 - Python Fundamentals\n"
                        "0 - Terminate\n "

                "======================================="
                 
                
                "\n\n\t 1  - Print Statements"
                    "\n\t 2  - Function"
                    "\n\t 3  - Variables"
                    "\n\t 4  - Conditionals"
                    "\n\t 5  - Operators"
                    "\n\t 6  - Loops "
                    "\n\t 7  - List"
                    "\n\t 0  - Terminate\n"
                
                    )
            
            pick = int(input("Choose a Number: "))
            
            if pick ==  1:
                statements()
            elif pick == 2:
                funct()
            elif pick == 3:
                var()
            elif pick == 4:
                con()
            elif pick == 5:
                oper()
            elif pick == 6:
                loo()
            elif pick == 7:
                lis()
            elif pick == 0:
                print("This Activities will be terminated.")

                sur = input("Are you sure? (Yes/No): ").strip().lower()       
                if sur == "yes":
                    delete()
                    print("The Activities will finally terminated.")
                    break

                elif sur == "no":
                    delete()
                    print("The Activities will still continue.")
                    continue

                else:
                        print("Invalid Input.")

            elif pick < 0:
                print("Error. Enter A Positive Number.")
            elif pick >= 8:
                print("Error.  Enter A number from the choices.")
            else:
                print("Invalid input")
        except ValueError:
                print("\nInvalid input, Please enter from the choices only.")
                continue
            
def statements():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\nprint('Hello, World!')\n"
                     "#output: Hello, world!\n")
                
                print("\nprint(123456789)\n"
                      "#output: 123456789\n\n")
                continue
                
            elif stat == "DESCRIPTION":
                print("\nJust put a print before the parenthesis then inside, the parenthesis put the data or text you want to print.")
                print("\nPrint statement display information to the user. Wether it's a simple text, calculated values or contents of variables.")
            
            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
                
                

            else:
                print("\nInvalid input, Enter from the choices given.\n")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.\n")
            continue
    
def funct():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()

            if stat == "EXAMPLE":
                print("\nBuilt-in functions:print(), input(), len(), max(), min(), sum(),\n\n"
                      "\nprint(Hello, world!)"
                      "\n#output: Hello, world!\n"
                      "\ninput('ENTER A NUMBER:')"
                      "\n#output: ENTER A NUMBER:\n"
                      "\nko = 'koil'"
                      "\nlen('koil')"
                      "\n#output: 4\n"
                      "\nmax(numbers)"
                      "\n#output maximum number\n"
                      "\nmin(numbers)"
                      "\n#output minimum number\n"
                      "\nsum(numbers)"
                      "\n#output summation of number\n\n"

                      )
                      
                print("User-defined function - can use/call the function just type the funtion name "
                "\ndef functions():"
                "\n\tprint('Hello, world!')\n"
                "\nfunctions()\n"
                "#output:Hello, World!\n"
                      )
                continue
                
            elif stat == "DESCRIPTION":
                print("\nFunctions are reusable blocks of code that perform specific task.")
                print("\nEssential for modularizing code, enhancing readability, and code reusability.\n")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
                
            else:
                print("\nInvalid input, Please enter from the choices given.\n")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.\n")
            continue
    
def var():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\nx = 10\n"
                "\nprint(x)"
                "\n#output: 10\n\n"
                "\nname = alice\n"
                "\nprint(name)\n"
                "output: alice\n\n")
                continue
                
            elif stat == "DESCRIPTION":
                print("\nVariables are symbolic names to memory locations where data is stored.")
                print("\nIt allows you to store, manipulate, and access data through code.\n")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
                
            else:
                print("\nInvalid input, Enter from the choices given.\n")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.\n")
            continue

def oper():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\n+ aaddition, 1 + 1.\n"
                      "- subtraction, 1 - 1\n"
                      "* multiplication, 8 * 8\n"
                      "/ division, 89 / 9\n"
                      "// floor devision, 1000//500\n"
                      "% modulus, 10 % 3\n"
                      "** exponentiation, 10 ** 2\n"
                      )
                
                print("== equal to, 10 == 5\n"
                     "!= not equal to, 10 != 5\n"
                      "> greater than, 10 > 5\n" 
                      "< less than, 10 < 5\n"
                      ">= greater than or eqal, 10 >= 5\n"
                      "<= less than or equal to, 10 <= 5\n"
                      
                      )
                continue
                
            elif stat == "DESCRIPTION":
                print("\nOperators determines the order of operation in complex expressions.\n")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
               
            else:
                print("\nInvalid input, Enter from the choices given.\n")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.\n")
            continue

def con():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\nif statements - If the condidtion is True, the intended code block is executed: otherwise, it's skipped.\n"
                "if age >= 18:"
                "\n\tprint('you are adult.')"
                "\n#output: you are adult.\n"
                      
                    )


                print("if-elif - This handle two possibilities: if false, and the if is true else statement execute"
                "\nelif age <= 18:\n"
                "\tprint('you are minor')\n"
                "#output: you are minor\n\n"     
                    )
                
                print("else - nested if statements - if statements inside other if statements to create more logic"
                "else:"
                "\n\tprint('Invalid Input')\n"
                "#output: Invalid input\n\n"

                    )
                
                print("\nboolean operators in condition - and, or, not operators used to modify conditions.\n")
                continue
                
            elif stat == "DESCRIPTION":
                print("\nConditionals in pyhton control the flow of execution based on wether certain conditons met.")
                print("\nIt allows the program to make decisions and execute different blocks of code depending on the state of your variables.\n")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
                
            else:
                print("\nInvalid input, Enter from the choices given.\n")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.")
            continue

def loo():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\nfor loops - It iterate over sequence(like a list, turple, string, or range).\n"
                "for i in range (1, 6):\n"
                "\tprint(cute)\n"
                      "#output: \ncute"
                      "\ncute"
                      "\ncute\n"
                      "cute\n\n"
                      "It iterate over sequence(like a list, turple, string, or range)."
                      
                        )
                
                print("while loops - while count < 5:"
                      "\tprint (count)\n"
                      "\tcount += 1\n"
                      "#output: it will print number 0 to 4")
                continue
                
            elif stat == "DESCRIPTION":
                print("\nIt is used to repeatedly execute block of code.")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break
                
            else:
                print("\nInvalid input, Enter from the choices given.")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.")
            continue

def lis():
    while True:
        try:
            print("\nEnter stop to go back from the menu")
            stat = input("Do you want to know the Definition or Example?(DESCRIPTON/EXAMPLE): ").upper().strip()
            
            if stat == "EXAMPLE":
                print("\nmy_list = [1,2,3,4,5].\n"
                "\tprint(my_list[0])\n"
                "#output(first element):\n"
                "1\n")
                continue
                
            elif stat == "DESCRIPTION":
                print("\nIt is an ordered, mutable(changeable) sequence of items.\n")
                print("It can contain different types of data.\n")

            elif stat == "STOP":
                print("\nProgram will go back to menu")
                menu()
                break

            else:
                print("\nInvalid input, Enter from the choices given.")
        
        except ValueError:
            print("\nInvalid input, Please enter from the choices only.")
            continue
    
menu()

"""Finished Project"""