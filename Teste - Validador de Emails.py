import re

def validar_email(email):
    # Padrão para validar endereços de e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False

# Exemplos de endereços de e-mail
emails = [
    "usuario@example.com",
    "joao.doe@email.com",
    "email_invalido@",
    "emailsem@dominio",
    "email_com_espaco@dominio.com",
]

for email in emails:
    if validar_email(email):
        print(f"{email} é um endereço de e-mail válido.")
    else:
        print(f"{email} não é um endereço de e-mail válido.")
