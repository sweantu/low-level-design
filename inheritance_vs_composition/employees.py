from abc import ABC, abstractmethod
from hr import PayrollSystem, SalaryPolicy, HourlyPolicy, CommissionPolicy
from contacts import AddressBook
from productivity import (
    ManagerRole,
    ProductivitySystem,
    SecretaryRole,
    SalesPersonRole,
    FactoryWorkerRole,
)

# class Employee(ABC):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.address = None


# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         Employee.__init__(self, id, name)


# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         Employee.__init__(self, id, name)


# class SalesPerson(Employee, SalesPersonRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         Employee.__init__(self, id, name)


# class FactoryWorker(Employee, FactoryWorkerRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hourly_rate):
#         HourlyPolicy.__init__(self, hours_worked, hourly_rate)
#         Employee.__init__(self, id, name)


# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hourly_rate):
#         HourlyPolicy.__init__(self, hours_worked, hourly_rate)
#         Employee.__init__(self, id, name)


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {"id": 1, "name": "Mary Poppins", "role": "manager"},
            {"id": 2, "name": "John Smith", "role": "secretary"},
            {"id": 3, "name": "Kevin Bacon", "role": "sales"},
            {"id": 4, "name": "Jane Doe", "role": "factory"},
            {"id": 5, "name": "Robin Williams", "role": "secretary"},
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.work(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
