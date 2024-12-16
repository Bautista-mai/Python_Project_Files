
def code14():
    sum = 0
    tut = True
    while tut:
        
            num = int(input("Please enter a number: "))
            if num == 0:
                print("Loop has now terminated")
                print(f"The sum of all the numbers you entered is: {sum}")
                break
            elif num < 0:
                print("Negative numbers are not allowed.")
                continue
            else:
                sum += num
                print(f"Added {num} to the sum. Current sum: {sum}")
                continue


