import csv

class User:
    def __init__(self, age, gender, income, utilities, entertainment, school_fees, shopping, healthcare):
        self.age = age
        self.gender = gender
        self.income = income
        self.utilities = utilities
        self.entertainment = entertainment
        self.school_fees = school_fees
        self.shopping = shopping
        self.healthcare = healthcare

    def save_to_csv(self, filename="user_data.csv"):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.age, self.gender, self.income, self.utilities, self.entertainment, self.school_fees, self.shopping, self.healthcare])
