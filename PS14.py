# Employee class
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        return self.salary * bonus_rate

    def show_info(self, bonus_rate):
        bonus = self.compute_bonus(bonus_rate)
        print("Employee Name:", self.first_name, self.last_name)
        print("Salary: $", self.salary)
        print("Bonus Rate:", bonus_rate)
        print("Bonus: $", bonus)


# Get input and test Employee class
print("Enter Employee Info")
emp_first = input("First Name: ")
emp_last = input("Last Name: ")
emp_salary = float(input("Salary: "))
bonus_rate = float(input("Enter Bonus Rate (e.g. 0.10 for 10%): "))

employee = Employee(emp_first, emp_last, emp_salary)
print("\n--- Employee Info ---")
employee.show_info(bonus_rate)

print("\n----------------------\n")

# Student class
class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == 'I':
            rate = 250.00
        else:
            rate = 500.00
        return self.enrolled_credits * rate

    def show_info(self):
        tuition = self.compute_tuition()
        print("Student Name:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Enrolled Credits:", self.enrolled_credits)
        print("Tuition Owed: $", tuition)


# Get input and test Student class
print("Enter Student Info")
stu_first = input("First Name: ")
stu_last = input("Last Name: ")
district_code = input("District Code (I or O): ")
credits = int(input("Enrolled Credits: "))

student = Student(stu_first, stu_last, district_code, credits)
print("\n--- Student Info ---")
student.show_info()
