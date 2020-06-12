class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:

    def __new__(cls, *args, **kwargs):
        if cls is Employee:
            raise TypeError("Employee não pode ser instanciada diretamente")
        return object.__new__(cls)

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        return self.salary * 0.15

    @staticmethod
    def get_hours():
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def get_department(self):
        return self.__departament.name

    def set_department(self, new_name):
        self.__departament = Department('{}'.format(new_name), 1)


class Seller(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, sell_number):
        self.__sales += sell_number

    def get_department(self):
        return self.__departament.name

    def set_department(self, new_name):
        self.__departament = Department('{}'.format(new_name), 2)

    def calc_bonus(self):
        return self.__sales * 0.15
