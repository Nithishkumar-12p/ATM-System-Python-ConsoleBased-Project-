# ATM-System-Python-ConsoleBased-Project-
A simple ATM System implemented in Python that allows users to withdraw money, deposit funds, generate PINs, and check mini-statements. The system uses a dictionary to store account details, including account number, user name, balance, and PIN.
This is a simple ATM simulation program created in Python. The system allows users to interact with a set of predefined accounts to perform basic banking operations such as withdrawals, deposits, pin generation, mini statements, and balance inquiries. 

This is a console-based ATM system that is useful for understanding basic banking operations, data structures, and Python programming concepts such as dictionaries, loops, and conditionals.

# Features

- *Withdrawal*: Allows the user to withdraw a specified amount from the account, provided sufficient funds are available.
- *Deposit*: Allows the user to deposit a specified amount into the account.
- *Pin Generation*: Enables the creation of a secure pin for an account if it doesn't exist.
- *Mini Statement*: Displays a mini statement of the account, showing details like name, account number, date of birth, and balance.
- *Balance Inquiry*: Displays the current balance of the account.
- *Account Validation*: Ensures the user enters valid account numbers and pins.

Menu Options:

When the program runs, you will be prompted with the following options:

1. *Withdrawal*: Enter the account number and pin to make a withdrawal.
2. *Deposit*: Enter the account number to make a deposit.
3. *Pin Generation*: Set a pin for your account if you haven't done so already.
4. *Mini Statement*: View account details and balance.
5. *Balance Inquiry*: Check the current balance of your account.
6. *Exit*: Close the program.

# Code Explanation

Key Elements:

- *Accounts Dictionary*: Stores the information for each account, including name, date of birth, balance, and pin.
- *Pin Check*: A pin is required for performing secure operations like withdrawal, balance inquiry, and mini statements.
- *Account Operations*: Users can perform operations such as withdrawing and depositing money, generating a pin, and checking the mini statement.

# Code Flow:

- The program runs in a loop, presenting a menu of operations to the user.
- Based on the selected option, the program asks for the account number and pin, and performs the corresponding action.
- After each operation, the program checks for valid inputs and ensures that transactions are only completed if the user provides the correct pin and sufficient funds (for withdrawals).
