def cut():
    import os

    while True:
        num = input("Enter a number(Enter 0 to stop): ")

        if num == "0":
            print("program stopped")
            break

        elif num % 2 == 0 :
            print("Number is even number")

cut()