from validarcpf import valida_cpf
import time

print()
print("Cadastro de usuários\n")

# input já retorna uma string, não é necessário usar str()
nome = input("Insira seu nome completo: ")
email = input("Insira seu email: ")

# Você esqueceu de pedir o CPF para o usuário!
while True:
    cpf_digitado = input("Insira seu CPF: ")
    print("\033[1m\nAnalisando seu CPF, por favor aguarde...\033[0m")
    time.sleep(5)
    if valida_cpf(cpf_digitado):
        break
    else:
        print("CPF inválido! Tente novamente.\n")


