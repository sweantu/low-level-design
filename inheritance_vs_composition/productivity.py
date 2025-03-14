class ProductivitySystem:

    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesPersonRole,
            "factory": FactoryWorkerRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(role_id)
        return role_type()

    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")


class ManagerRole:
    def work(self, hours):
        print(f"screams and yells for {hours} hours.")


class SecretaryRole:
    def work(self, hours):
        print(f"expends {hours} hours doing office paperwork.")


class SalesPersonRole:
    def work(self, hours):
        print(f"expends {hours} hours on the phone.")


class FactoryWorkerRole:
    def work(self, hours):
        print(f"manufactures gadgets for {hours} hours.")
