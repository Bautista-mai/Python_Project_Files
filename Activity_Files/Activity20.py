def Act20():
    continu = True
    count = 0

    while continu == True:
        name = input("Enter a name(Enter stop to stop the program): ").upper().strip()

        if name == "STOP":
            print("The loop has now stopped")
            print(f"You have entered {count} number of names")
            break

        else:
            count += 1
            continue

