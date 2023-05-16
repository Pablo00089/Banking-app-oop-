# Banking system using OOP
# ------------------------

# Parent Class
class User():
    
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender 
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
        
# u1 = User("Johan", 21, "Male")
# u1.show_details

# Child Class
class Bank(User):
    
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: ", self.balance, "Kč")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: ", self.balance, "Kč")
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance, "Kč")
            
    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: ", self.balance, "Kč")
            
u1 = Bank("Johan", 21, "Male")
u1.deposit(1000)
u1.deposit(1000)
u1.deposit(1000)
u1.withdraw(500)
u1.withdraw(500)
u1.withdraw(1000)
u1.withdraw(1000)
u1.withdraw(1000)
u1.show_details()
u1.view_balance()