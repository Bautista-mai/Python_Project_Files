def code16():

    class BankAccount:

        def __init__(self, name, bal):
            self.name = name
            self.bal = bal

        def dep(self, amount):
            if amount > 0:
                self.bal += amount
                print(f"Deposited {amount:.2f} PHP. Current balance: {self.bal:.2f} PHP")
            else:
                print("Invalid deposit amount.")

        def wit_draw(self, amount):
            if 0 < amount <= self.bal:
                self.bal -= amount
                print(f"Withdrew {amount:.2f} PHP. Current balance: {self.bal:.2f} PHP")
            else:
                print("Insufficient funds or invalid withdrawal amount.")

        def get_bal(self):
            return self.bal

    # Denomination function OUTSIDE the class
    def denom(amount):
        deno = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        deno_count = {}

        for d in deno:
            deno_count[d] = amount // d
            amount %= d

        return deno_count

    def run():
        acc = None
        while True:
            print("\nBanking Program")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Terminate")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter account name: ")
                initial_deposit = float(input("Enter initial deposit amount: "))
                acc = BankAccount(name, initial_deposit)
                print(f"\n\nAccount created for {name} with initial deposit of {initial_deposit:.2f} PHP.")

            elif choice == "2":
                if acc:
                    amount = float(input("Enter deposit amount: "))
                    acc.dep(amount)
                else:
                    print("\nPlease create an account first.")

            elif choice == "3":
                if acc:
                    amount = float(input("Enter withdrawal amount: "))
                    acc.wit_draw(amount)
                else:
                    print("\nPlease create an account first.")

            elif choice == "4":
                if acc:
                    balance = acc.get_bal()
                    print(f"\n\nCurrent balance: {balance:.2f} PHP")
                else:
                    print("\nPlease create an account first.")

            elif choice == "5":
                print("\n\nTerminating program...")
                while True:
                    decision = input("\n\tDo You Want To Denominate Your Current Balance? [Yes / No]: ").strip().upper()

                    if decision == "YES":
                        if acc:
                            balance = acc.get_bal()
                            breakdown = denom(balance)  # Call the denomination function
                            print("\nDenomination of Current Balance:")
                            for note, count in breakdown.items():
                                print(f"PHP {note}: {count}")
                        else:
                            print("\nPlease create an account first.")
                        break

                    elif decision == "NO":
                        print("\n\tDenomination Cancelled.")
                        break

                    else:
                        print("\n\n\tError. Wrong Input.")
                        continue

                break  # Exit program after denomination check

            else:
                print("\n\nInvalid choice. Please try again.")

    if __name__ == "__main__":
        run()

code16()
