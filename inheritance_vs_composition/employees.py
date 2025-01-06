from abc import ABC, abstractmethod
from hr import SalaryPolicy, HourlyPolicy, CommissionPolicy
from productivity import ManagerRole, SecretaryRole, SalesPersonRole, FactoryWorkerRole


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        Employee.__init__(self, id, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        Employee.__init__(self, id, name)


class SalesPerson(Employee, SalesPersonRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        Employee.__init__(self, id, name)


class FactoryWorker(Employee, FactoryWorkerRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
        Employee.__init__(self, id, name)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
        Employee.__init__(self, id, name)
