def denom(amount):

    deno = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    deno_count = {}

    for deno in deno:
        deno_count[deno] = amount // deno
        amount %= deno


    return deno_count


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
            break
        else:
            print("\n\nInvalid choice. Please try again.")
            
            while True:

                desicion = input("\n\tDo You Want To Denominate Your Current Balance? [Yes / No]: ").strip().upper()

                if desicion == "YES":

                    ans1 = balance // 1000
                    num1 = balance % 1000

                    ans2 = num1 // 500
                    num2 = num1 % 500

                    ans3 = num2 // 200
                    num3 = num2 % 200

                    ans4 = num3 // 100
                    num4 = num3 % 100

                    ans5 = num4 // 50
                    num5 = num4 % 50

                    ans6 = num5 // 20
                    num6 = num5 % 20

                    ans7 = num6 // 10
                    num7 = num6 % 10

                    ans8 = num7 // 5
                    num8 = num7 % 5

                    ans9 = num8 // 1

                    print(f"\n\n\t\tThe Current Balance Of {name} is: ₱{account[name]}")
                    print(f"\n\n\t\t₱1000 - {ans1}"
                    f"\n\t\t₱500 - {ans2}"
                    f"\n\t\t₱200 - {ans3}"
                    f"\n\t\t₱100 - {ans4}"
                    f"\n\t\t₱50 - {ans5}"
                    f"\n\t\t₱20 - {ans6}"
                    f"\n\t\t₱10 - {ans7}"
                    f"\n\t\t₱5 - {ans8}"
                    f"\n\t\t₱1 - {ans9}")
                
                    break

                elif desicion == "NO":
                        print("\n\tDenomination Cancelled.")
                        return

                else:
                    print("\n\n\tError. Wrong Input.")
                    continue
            
if __name__ == "__main__":
    run()