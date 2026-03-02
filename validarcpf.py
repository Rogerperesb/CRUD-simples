from validate_docbr import CPF

def valida_cpf(num_cpf):
    """Valida um CPF e retorna True ou False."""
    cpf = CPF()
    return cpf.validate(num_cpf)

if __name__ == "__main__":
    # O código abaixo só será executado se você rodar este arquivo diretamente
    num = input("Digite seu CPF para teste: ")
    if valida_cpf(num):
        print("CPF Válido!")
        print("Formatado:", CPF().mask(num))
    else:
        print("CPF Inválido!")
