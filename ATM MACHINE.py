#ATM System: 
#Design a simple ATM system with multiple users and functionalities like checking balance, depositing, withdrawing, and transferring money between accounts.

class ATM_MACHINE:

    def __init__(self):
        self.name=input("Enter the name of the ATM: ")
        self.location=input(f"Enter the location of {self.name}: ")
        self.card_number=int(input("Enter the card number: "))
        self.holder=input("Enter the customer name: ")
        self.pin=int(input("Enter the pin number: "))
        self.balance=float(input("Enter the total balance of your debit card: "))
        print ("\n")

    def display_info(self):
        print (f"ATM NAME IS {self.name}")
        print (f"{self.name} is located in {self.location}")
        print (f"{self.holder} is the customer name")
        print (f"Your's debit card number is {self.card_number}")
        print (f"Debit Card's pin number is {self.pin}")
        print ("\n")


    def Punching(self):
        self.entered_pin=int(input("Enter your pin: "))
        if self.entered_pin==self.pin:
            print ("Authorization is Successful")
            return True
        else:
            print ("Error, Authorization failed")
            return False
        
    def display_balance(self):
        print (f"AVALIABLE BALANCE IS Rs {self.balance: .2f}")

    def credit(self,amount):
        self.balance+=amount
        print (f"Amount of Rs {amount} has been deposited to your account number XXXXX650")

    def credit_total(self):
        print (f"Avaliable Balance is Rs {self.balance: .2f}")

    def debit(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print (f"Amount of Rs {amount} has been debited from account no XXX650 in {self.name}")
        else:
            print ("Insufficient Fund")

    def debit_total(self):
        print (f"Avaliable balance is Rs {self.balance: .2f}")

    def menu(self):
        print(f"\nWelcome Mr. {self.holder}")
        while True:
            print ("\nATM MENU ARE AS FOLLOW")
            print ("1. Check Balance")
            print ("2. Credit the amount")
            print ("3. Debit the amount")
            print ("4. Exit")

            choice=int(input("\nEnter your choice: "))

            if choice==1:
                self.display_balance()

            elif choice==2:
                credit_amount=float(input("Enter the amount to credit is Rs "))
                self.credit(credit_amount)

            elif choice==3:
                debit_amount=float(input("Enter the amount to debit is Rs "))
                self.debit(debit_amount)

            elif choice==4:
                print (f"Thank You for choosing {self.name}. Visit again!!!")
                break
            else:
                print ("Invalid Choice")

A=ATM_MACHINE()
A.Punching()
A.display_info()
A.menu()



        
