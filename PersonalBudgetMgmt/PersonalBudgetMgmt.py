#Task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    #Task 2
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name
    def get_category_name(self):
        return self.__category_name
    def set_allocated_budget(self, new_budget):
        self.__allocated_budget = new_budget
        new_budget >= 0
    def get_allocated_budget(self):
        self.__allocated_budget = 500
        return self.__allocated_budget

    #Task 3
    def add_expense(self, amount):
        self.expense = amount
        print(f"\nYou have spent ${amount} dollars from your alloted budget.")

    #Task 4
    def display_category_summary(self):
        print(f"\nCategory: {self.__category_name}")
        print(f"Alloted Budget: ${self.__allocated_budget}")
        print(f"Amount Remaining After Expenses: ${self.__allocated_budget - self.expense}\n")

food_category = BudgetCategory('Food', 500)
food_category.add_expense(150)
food_category.display_category_summary()