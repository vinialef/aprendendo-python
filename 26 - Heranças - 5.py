class EmployeeOverview:
    def __str__(self):
        return f"{self.__class__.__name__}: {'\n'.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"


class EmployeeInfo(EmployeeOverview):
    def __init__(self,name,employee_id,department,**kw):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        super().__init__(**kw)

class EmployeeContacts(EmployeeOverview):
    def __init__(self,email,phone,**kw):
        self.email=email
        self.phone=phone
        super().__init__(**kw)

class Employee(EmployeeInfo,EmployeeContacts):
    def __init__(self,name,employee_id,department,position,salary,email,phone):
        super().__init__(name=name,employee_id=employee_id,department=department,email=email,phone=phone)
        self.position = position
        self.salary = salary
   
# Exemplo de uso
employee = Employee(name=input(), employee_id='1234', position='Manager', salary=70000,department='Escritório',email='seuze@email.com',phone="84 9181907654")
print("\nInformações do Funcionário:\n")
print(employee)
