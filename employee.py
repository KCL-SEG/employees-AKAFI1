"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract="", hours="", commission="", hourlyPay="", salaryPay="", fixedCommission="", noContracts="", contractPay=""):
        self.name = name
        self.contract = contract
        self.hours = hours
        self.commission = commission
        self.hourlyPay = hourlyPay
        self.salaryPay = salaryPay
        self.fixedCommission = fixedCommission
        self.noContracts = noContracts
        self.contractPay = contractPay

    def contract_pay(self):
        if self.contract == 'monthly':
            return self.salaryPay
        else:
            return self.hourlyPay * self.hours

    def commission_pay(self):
        if self.commission == 'bonus':
            return self.fixedCommission
        else:
            return self.noContracts * self.contractPay

    def get_pay(self):
        totalPay = self.contract_pay()
        if self.commission:
            totalPay += self.commission_pay()
        return totalPay

    def __str__(self):
        printStr = f"{self.name} works on a "
        if self.contract == 'monthly':
            printStr += f"{self.name} has a monthly salary of {self.contractPay}"
        else:
            printStr += f"{self.name} has a contract of {self.hours} hours at {self.hourlyPay}/hour"
        if self.commission:
            if self.commission == 'bonus':
                printStr += f" and receives a bonus commission of {self.fixedCommission}."
            else:
                printStr += f" and receives a commission for {noContracts} contract(s) at {contractPay}/contract."
        printStr += f" {self.name}'s total pay is {self.get_pay()}."
        print(printStr)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
