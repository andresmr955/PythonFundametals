import random

class Patrimony:
    def __init__(self):
        self.contributed_capital = random.randint(1000, 10000)
        self.earnings = random.randint(1000, 10000)
        

    def calculate_patrimony(self):
        list_actives = []
        list_actives.append(self.contributed_capital)
        list_actives.append(self.earnings)

        total_patrimony = 0
        for count in list_actives:
            total_patrimony += count
        
        return total_patrimony
    
class Passive:
    def __init__(self):
        self.leasing = random.randint(1000, 10000)
        self.counts_to_pay = random.randint(1000, 10000)

    def calculate_passive(self):
        concepts = []
        concepts.append(self.leasing)
        concepts.append(self.counts_to_pay)

        total_passive = 0
        for count in concepts:
            total_passive += count
        
        return total_passive

class Active:
    def __init__(self, patrimony_obj, passive_obj):
        self.patrimony_obj = patrimony_obj
        self.passive_obj = passive_obj

    def calculate_active(self):
        total_active = self.passive_obj.calculate_passive() + self.patrimony_obj.calculate_patrimony()

        return total_active

    def balance(self):
        active = self.calculate_active()
        passive = self.passive_obj.calculate_passive()
        patrimony = self.patrimony_obj.calculate_patrimony()

        if active == passive + patrimony:
            # print("The balance is balanced ")
            return True
        else:
            # print("The balance is not balanced")
            return False

class MonthlyBalance:
    def __init__(self, month):
        self.month = month
        self.patrimony = Patrimony()
        self.passive = Passive()
        self.active = Active(self.patrimony, self.passive)

    def calculate(self):
        self.total_patrimony = self.patrimony.calculate_patrimony()
        self.total_passive = self.passive.calculate_passive()
        self.total_active = self.active.calculate_active()
        self.balanced = self.active.balance()

    def monthly_row(self):
        return [self.month, self.total_patrimony, self.total_passive, self.total_active, self.balanced]

