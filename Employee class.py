
class Employee:
    count = 0

    def __init__(self, empno, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            print("Basic, DA and HRA cannot be negative.")
            raise SystemExit

        self.empno = empno
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        Employee.count -= 1

    def __str__(self):
        return (f"Employee Number: {self.empno}\n"
                f"Name: {self.name}\n"
                f"Department: {self.dept}\n"
                f"Basic: {self.basic}\n"
                f"DA: {self.da}\n"
                f"HRA: {self.hra}\n"
                f"Salary: {self.salary()}")


# Creating employee objects
e1 = Employee(101, "Rahul", "IT", 20000, 5000, 3000)
e2 = Employee(102, "Aman", "HR", 25000, 6000, 4000)

print(e1)
print()
print(e2)

print("\nTotal employees:", Employee.count)
