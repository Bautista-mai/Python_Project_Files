
def code7():

    grocery = input("Did you buy a grocery? (yes?no): ")

    if grocery == "yes":
        name = input("What is your name? ")
        age = int(input("How old are you? "))
        
        if age <= 0 or age >120:
            print("I'm sorry but your age is invalid")
        else:    
            item = input("name of the item? ")
            amo = int(input("amount of the item? "))
            
            if amo <= 0:
                print("Check again there must be a mistake")
                
            else:
                amount = float(input("Amount given: "))            
                
                if amount <=0:
                    print("Check again there must be a mistake")
                    
                else:

                    calc1 = amo * 0.123
                    calc2 = amo + calc1
                        
                    calc3 = calc2 * 0.052
                    calc4 = calc2 - calc3
                                    
                    final1 = amount - calc2
                    final2 = amount - calc4

                    if age >= 1 and age <= 59:
                        if final1 < 0:
                            print(f"Hello {name} , the amount you've entered is short by {round(final1, 2)}. Please check again there must be a mistake ")
                        else:
                            print(f"Hello {name}, you purchased a {item}, with a Price of {amo} plus a 12.3% tax ({round(calc1, 2)}).Total Cost: {round(calc2, 2)} Amount Given: {amount} Change: {round(final1, 2)}  ")

                    elif age >= 60 and age <= 120:
                        if final2 < 0:
                            print(f"Hello {name} , the amount you've entered is short by {round(final2, 2)}. Please check again there must be a mistake")
                        else:
                            print(f"Hi  {name}, you purchased a {item}, with a Price of {amo} plus a 12.3% tax ({round(calc1, 2)}), and since you're a senior , you have a 5.2% discount ({round(calc3, 2)}).Total Cost: {round(calc4, 2)} Amount Given: {amount} Change: {round(final2, 2)}  ")

    elif grocery == "no":
        print("Thank you for visiting")

    else:
        print("Try again this can only be answered by yes or no ")    