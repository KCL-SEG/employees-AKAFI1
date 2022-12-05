"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class FixedCommission:
    def __init__(self, bonus) -> None:
        self.description = f"bonus commission of {bonus}"
        self.value = bonus

class ContractCommission:
    def __init__(self, contract_num, price_per_contract) -> None:
        self.description = f"commission for {contract_num} contract(s) at {price_per_contract}/contract"
        self.value = contract_num * price_per_contract

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return self.get_base_pay() + (self.commission.value if self.commission else 0)

    def __str__(self):
        return f"{self.name} works on a {self.get_contract_desc()}" + \
            (f" and receives a {self.commission.description}" if self.commission else "") + \
                f". Their total pay is {self.get_pay()}."

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission=None):
        super().__init__(name, commission)
        self.salary = salary

    def get_contract_desc(self):
        return f"monthly salary of {self.salary}"
    
    def get_base_pay(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, name, hours, hourly_pay, commission=None):
        super().__init__(name, commission)
        self.hours = hours
        self.hourly_pay = hourly_pay

    def get_contract_desc(self):
        return f"contract of {self.hours} hours at {self.hourly_pay}/hour"

    def get_base_pay(self):
        return self.hours * self.hourly_pay


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
