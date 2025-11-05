class Employee:
    def __init__(self, salary_uzs):
        self.salary_uzs = salary_uzs

    @property
    def salary_usd(self):
        return self.salary_uzs / 12000

    @salary_usd.setter
    def salary_usd(self, value):
        self.salary_uzs = value * 12000


emp = Employee(2400000)
print(emp.salary_usd)
emp.salary_usd = 300
print(emp.salary_uzs)
