#python bank prgm

def show_balance(balance):
    print(f"You balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))

    if amount < 0:
        print("Not a valid amount to be deposited")
        return 0
    else:
        return amount

    print()

def withdraw(balance):
     amount = float(input("Enter amount to be withdrawn: "))

     if amount > balance:
        print("Not valid u dont have enough funds")
        return 0
     elif amount < 0:   
         print("Amount needs to be greater than zero")
         return 0
     else:
        return amount

def main():
    balance=0
    is_running= True

    while is_running:
        print("--------------------------------------")
        print("    The banking program in python     ")
        print("--------------------------------------")
        print("1.Show Balance")
        print("2.Make Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter you choice (1-4): ")
        print()

        if choice == "1":
            show_balance(balance)
        elif choice =="2":
            balance+=deposit()
        elif choice =="3":
            balance-=withdraw(balance)
        elif choice =="4":
            is_running = False
        else:
            print("That is not a valid choice")
        print()
    print("---------------------")
    print("Thank you come again.")
    print("---------------------")
if __name__ == '__main__':
    main()