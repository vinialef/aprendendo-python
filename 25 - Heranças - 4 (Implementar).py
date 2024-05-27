class EmployeeInfo:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'John Doe')
        self.employee_id = kwargs.get('employee_id', '0000')
        self.department = kwargs.get('department', 'General')
        self.email = kwargs.get('email', 'seuze@email.com')
        self.phone = kwargs.get('phone', '84 918190765')


class Employee(EmployeeInfo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = kwargs.get('position', 'Employee')
        self.salary = kwargs.get('salary', 50000)

# Exemplo de uso
employee = Employee(name='Alice Smith', employee_id='1234',department= 'Escritório', position='Manager', salary=70000)
print("Informações do Funcionário:")
print("Nome:", employee.name)
print("ID do Funcionário:", employee.employee_id)
print("Departamento:", employee.department)
print("Cargo:", employee.position)
print("Salário:", employee.salary)

print("Contatos:")
print("Email:",employee.email)
print("Telefone:",employee.phone)

#implementar pedindo o cargo e mostranto o salário para determinado cargo
#Gerando um email automatico de acordo com o nome
#Gerar um novo id de acordo com o cargo