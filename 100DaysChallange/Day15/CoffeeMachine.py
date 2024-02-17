import art


class CoffeeMachine:

    def __init__(self):
        self.milk = 100
        self.coffee = 100
        self.water = 100
        self.balance = 0

    def printReport(self):
        print(self.milk)
        print(self.coffee)
        print(self.water)
        print(self.balance)

    @staticmethod
    def makeCoffeeMachineOff():
        return 0

    def checkResource(self, req_milk, req_coffee, req_water):
        return True if (req_milk < self.milk and req_coffee < self.coffee and req_water < self.water) else False

    def makeCoffee(self, item):
        if item == 'expresso':
            if self.checkMoney(50):
                if self.checkResource(req_milk=25, req_coffee=15, req_water=20):
                    self.milk -= 25
                    self.coffee -= 15
                    self.water -= 20
                    self.balance += 50
                    print(f"Here is your {item} Thanks!!!!")
                else:
                    print(f"sorry we dont have enough resources for your {item}")
            else:
                print("you dont have enough cash please try again")
                self.startCoffeeMachine()
        elif item == 'cappuccino':
            if self.checkMoney(70):
                if self.checkResource(req_milk=30, req_coffee=20, req_water=25):
                    self.milk -= 30
                    self.coffee -= 20
                    self.water -= 25
                    self.balance += 70
                    print(f"Here is your {item} Thanks!!!!")
                else:
                    print(f"sorry we dont have enough resources for your {item}")
            else:
                print("you dont have enough cash please try again")
                self.startCoffeeMachine()
        if item == 'latte':
            if self.checkMoney(40):
                if self.checkResource(req_milk=10, req_coffee=30, req_water=20):
                    self.milk -= 10
                    self.coffee -= 30
                    self.water -= 20
                    self.balance += 40
                    print(f"Here is your {item} Thanks!!!!")
                else:
                    print(f"sorry we dont have enough resources for your {item}")
            else:
                print("you dont have enough cash please try again")
                self.startCoffeeMachine()

    def startCoffeeMachine(self):
        order = input(f"what would you like ??? (expresso / Capuccino / Latte)").lower()
        if order == 'report':
            self.printReport()
        elif order == 'off':
            self.makeCoffeeMachineOff()
            return 0
        elif order in ('expresso', 'cappuccino', 'latte'):
            self.makeCoffee(order)
        else:
            print('you entered invalid option please try again')
            self.startCoffeeMachine()
        print('your order is completed Thanks!!! \n ')
        self.startCoffeeMachine()

    @staticmethod
    def printBanner():
        print(art.logo)

    @staticmethod
    def checkMoney(req_minimum):
        print("what money you have ?? \n")
        _100 = int(input('how many 100 note you have ?'))
        _50 = int(input('how many 50 note you have ?'))
        _10 = int(input('how many 10 note you have ?'))
        return True if req_minimum < (_100 * 100 + _50 * 50 + _10 * 10) else False


# Resources
obj1 = CoffeeMachine()
obj1.printBanner()
obj1.startCoffeeMachine()
print("Thankyou...")
