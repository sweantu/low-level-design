# import employees
# import hr
# import productivity
# import contacts

# manager = employees.Manager(1, "Mary Poppins", 3000)
# manager.address = contacts.Address("121 Admin Rd", "Concord", "NH", "03301")
# secretary = employees.Secretary(2, "John Smith", 1500)
# secretary.address = contacts.Address("67 Paperwork Ave.", "Manchester", "NH", "03101")
# sales_guy = employees.SalesPerson(3, "Kevin Bacon", 1000, 250)
# factory_worker = employees.FactoryWorker(4, "Jane Doe", 40, 15)
# temporary_secretary = employees.TemporarySecretary(5, "Robin Williams", 40, 9)
# employees = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
#     temporary_secretary,
# ]

# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)


from hr import HourlyPolicy, PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDatabase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(55)
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
