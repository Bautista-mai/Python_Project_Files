import os

from Activity_Files import ( 

                    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7,
                    Activity8, Activity9, Activity10, Activity11, Activity12, Activity13, Activity14,
                    Activity15, Activity16, Activity17, Activity18, Activity19, Activity20, Activity21,
                    Activity22, Activity23, Activity24, Activity25

                    )

from Code_Challenge_Files import (

                    Code_Challenge1, Code_Challenge2, code_challenge3, code_challenge4, code_challenge5,
                    code_challenge6, code_challenge7, Code_Challenge8, code_challenge9, code_challenge10,
                    code_challenge11, code_challenge12, code_challenge13, code_challenge14, code_challenge15,
                    code_challenge16    

                    )

def Acts():
        while True:
            try:
                print("\nCOMPILATION OF PROJECTS\n"
                        "--------------------------\n"
                        "---------> MENU <---------\n"
                
                
                        "\n1 - Activities Compilations\n"
                        "2 - Code_challenge_Compilations\n"
                        "0 - Terminate\n"
                
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
                        print("The Activities will finally terminated")
                        break

                    elif sur == "no":
                        delete()
                        print("The Activities will still continue")
                        continue

                    else:
                        print("Invalid Input")

                elif cho < 0:
                    print("Error. Enter A Positive Number.")
                elif cho >= 26:
                    print("Error.  Enter A number from the choices")
                else:
                    print("Invalid input")
            
            except ValueError:
                print("Invalid, Please enter from the choices only")
                continue
        
def codes():
    while True:
        try:
            print("\nCOMPILATION OF PROJECTS\n"
                        "--------------------------\n"
                        "---------> MENU <---------\n"
                
                
                        "\n1 - Activities Compilations\n"
                        "2 - Code_challenge_Compilations\n"
                        "0 - Terminate "
                
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

            choi = int(input("Choose a Number:"))
        
            if choi ==  1:
                Code_Challenge1.code1()
            elif choi == 2:
                Code_Challenge2.code2()
            elif choi == 3:
                code_challenge3.code3()
            elif choi == 4:
                code_challenge4.code4()
            elif choi == 5:
                code_challenge5.code5()
            elif choi == 6:
                code_challenge6.code6()
            elif choi == 7:
                code_challenge7.code7()
            elif choi == 8:
                Code_Challenge8.code8()
            elif choi == 9:
                code_challenge9.code9()
            elif choi == 10:
                code_challenge10.code10()
            elif choi == 11:
                code_challenge11.code11()
            elif choi == 12:
                code_challenge12.code12()
            elif choi == 13:
                code_challenge13.code13()
            elif choi == 14:
                code_challenge14.code14()
            elif choi == 15:
                code_challenge15.code15()
            elif choi == 16:
                code_challenge16.code16()
        
            elif choi == 0:
                    print("This Activities  be terminated")

                    sur = input("Are you sure? (Yes/No): ").strip().lower()          
                    if sur == "yes":
                        delete()
                        print("The Activities will finally terminated")
                        break

                    elif sur == "no":
                        delete()
                        print("The Activities will still continue")
                        continue

                    else:
                        print("Invalid Input")

            elif choi < 0:
                print("Error. Enter A Positive Number.")
            elif choi >= 17:
                print("Error.  Enter A number from the choices")
            else:
                print("Invalid input")
        
        except ValueError:
                print("Invalid, Please enter from the choices only")
                continue


def delete():
    os.system("cls")

def menu():
    while True:
        try:
            print("\nCOMPILATION OF PROJECTS\n"
                "--------------------------\n"
                "---------> MENU <---------\n"
                
                
                "\n1 - Activities Compilations\n"
                "2 - Code_challenge_Compilations\n"
                "0 - Terminate\n"
                
                )
            
            choose = int(input("Choose A number: "))

            if choose == 1:
                    Acts()
            elif choose == 2:
                    codes()
            elif choose == 0:
                print("This Activities  be terminated")

                sur = input("Are you sure? (Yes/No): ").strip().lower()       
                if sur == "yes":
                    delete()
                    print("The Activities will finally terminated")
                    break

                elif sur == "no":
                    delete()
                    print("The Activities will still continue")
                    continue

                else:
                        print("Invalid Input")

            elif choose < 0:
                print("Error. Enter A Positive Number.")
            elif choose >= 26:
                print("Error.  Enter A number from the choices")
            else:
                print("Invalid input")
        except ValueError:
                print("Invalid input, Please enter from the choices only")
                continue

menu()
