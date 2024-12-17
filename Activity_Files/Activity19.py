def Act19():
    isContinue = True

    while isContinue:
        name = input("Give me name(Enter stop to terminate the program): ")

        if name.lower() == "stop":
            print("Loop terminated")
            break

            isContinue = False
        else:
            print(f"Hi {name}")
            continue

