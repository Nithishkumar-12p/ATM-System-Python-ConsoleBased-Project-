print("\nWelcome to ATM\n")

accounts = {
    1001: ["User 1", "24-08-2024", 10000, 2408],
    1002: ["User 2", "16-07-2024", 20000, 1234],
    1003: ["User 3", "20-01-2024", 5000, None]
}

dobm = {1: "January", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini statement")
    print("5. Exit")
    option = int(input("Enter Your Option: "))
    print()

    match option:
        case 1:
            accno = int(input("Enter Account Number: "))
            if accno not in accounts:
                print("Account Does not Exist!")
            else:
                pin = int(input("Enter Pin: "))
                if accounts[accno][-1] is None:
                    print("Generate Pin")
                elif accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficient Funds")
                    else:
                        print("Withdrawal Successful!")
                        accounts[accno][-2] -= amt
            print()

        case 2:
            accno = int(input("Enter Account Number: "))
            if accno not in accounts:
                print("Account does not Exist")
            else:
                amt = int(input("Enter Amount to Deposit: "))
                accounts[accno][-2] += amt
                print("Deposit Successful")
            print()

        case 3:
            accno = int(input("Enter Account Number: "))
            if accno not in accounts:
                print("Account Does not Exist")
            else:
                if accounts[accno][-1] is None:
                    pin = int(input("Enter Pin: "))
                    cpin = int(input("Confirm Pin: "))
                    if pin != cpin:
                        print("Pin Does not Match")
                    else:
                        accounts[accno][-1] = pin
                        print("Pin Generated Successfully")
                else:
                    print("Pin Already Exists")
            print()

        case 4:
            accno = int(input("Enter Account Number: "))
            if accno not in accounts:
                print("Account Does not Exist")
            else:
                pin = int(input("Enter Pin: "))
                if pin != accounts[accno][-1]:
                    print("Invalid Pin")
                else:
                    print(f"Name: {accounts[accno][0]}")
                    print(f"Account Number: {accno}")
                    dob = accounts[accno][1].split("-")
                    date, month, year = dob[0], dobm[int(dob[1])], dob[2]
                    print(f"Date of Birth: {date}-{month}-{year}")
                    print(f"Account Balance: {accounts[accno][-2]}")
            print()

        case 5:
            print("Exiting ATM... Have a nice day!")
            break

        case _:
            print("Invalid Option! Please try again.")
            print()
