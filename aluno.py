from re import match, sub

class Aluno:
    def __init__(self):
        self.nome = None
        self.email = None
        self.cpf = None
        self.telefone = None

    def valida_nome(self):
        nome = input("Digite seu nome: ")
        self.nome = nome

        format = r"^[A-Za-z]{2,100}\D"

        while True:
            if match(format, nome):
                break
            else:
                nome = input("Digite um nome válido: ")
                self.nome = nome

    def valida_cpf(self):
        cpf = input("Digite seu CPF: ")
        self.cpf = cpf

        cpf = ''.join(filter(str.isdigit, cpf))

        while True:
            if len(cpf) != 11 or cpf == cpf[0] * 11:
                cpf = input("CPF inválido, digite novamente: ")
                self.cpf = cpf
                continue

            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            resto = soma % 11

            if resto < 2:
                digito_verificador_1 = 0
            else:
                digito_verificador_1 = 11 - resto

            if int(cpf[9]) != digito_verificador_1:
                cpf = input("CPF inválido, digite novamente: ")
                self.cpf = cpf
                continue

            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            resto = soma % 11
            if resto < 2:
                digito_verificador_2 = 0
            else:
                digito_verificador_2 = 11 - resto

            if int(cpf[10]) != digito_verificador_2:
                cpf = input("CPF inválido, digite novamente: ")
                self.cpf = cpf
                continue
            break

    def valida_telefone(self):
        telefone = input("Digite seu telefone: ")
        self.telefone = telefone

        format = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"

        while True:
            if match(format, telefone):
                break
            else:
                telefone = input("Digite um número de telefone/celular válido: ")
                self.telefone = telefone

    def valida_email(self):
        email = input("Digite seu email: ")
        self.email = email

        format = r"^[a-zA-Z0-9._%+-]{3,64}@[a-zA-Z0-9.-]{2,20}\.[a-zA-Z]{2,10}$"

        while True:
            if match(format, email):
                break
            else:
                email = input("Digite um email válido: ")
                self.email = email

    def __str__(self):
        reformat_telefone =  sub(r"\(?(\d{2})\)?\s?(\d{4,5})-?(\d{4})", r"(\1) \2-\3", self.telefone)
        reformat_cpf = sub(r"(\d{3}).?(\d{3}).?(\d{3})-?(\d{2})", r"\1.\2.\3-\4", self.cpf)
        return (f"\nNome: {self.nome}".title() +
                f"\nEmail: {self.email}"
                f"\nCPF: {reformat_cpf}"
                f"\nTelefone: {reformat_telefone}")