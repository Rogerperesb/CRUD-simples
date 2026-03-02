import json
import os
import time
from validarcpf import valida_cpf

# Arquivo para salvar os dados em formato JSON, garantindo que os dados não se percam
ARQUIVO_DADOS = "usuarios.json"

def carregar_usuarios():
    """Lê o arquivo JSON e retorna a lista de usuários, ou uma lista vazia se não existir."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_usuarios(usuarios):
    """Salva a lista de usuários no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def criar_usuario(usuarios):
    """(C)reate: Cadastra um novo usuário utilizando a validação de CPF."""
    print("\n--- Cadastro de Usuário ---")
    nome = input("Insira seu nome completo: ")
    email = input("Insira seu email: ")
    
    while True:
        cpf_digitado = input("Insira seu CPF: ")
        
        print("\033[1m\nAnalisando seu CPF, por favor aguarde...\033[0m")
        time.sleep(2) # Tempo reduzido (originalmente era 5, mudei para 2 ficar mais dinâmico)
        
        if valida_cpf(cpf_digitado):
            # Verifica se o CPF já está cadastrado
            cpf_limpo = ''.join(filter(str.isdigit, cpf_digitado))
            ja_existe = any(u.get('cpf') == cpf_limpo for u in usuarios)
            
            if ja_existe:
                print(f"Erro: O CPF já está cadastrado no sistema!\n")
                return
            break
        else:
            print("CPF inválido! Tente novamente.\n")

    novo_usuario = {
        "nome": nome,
        "email": email,
        "cpf": ''.join(filter(str.isdigit, cpf_digitado)) # Salva só números
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("\nUsuário cadastrado com sucesso!")

def listar_usuarios(usuarios):
    """(R)ead: Lista todos os usuários cadastrados."""
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. Nome: {u['nome']} | Email: {u['email']} | CPF: {u['cpf']}")

def atualizar_usuario(usuarios):
    """(U)pdate: Atualiza os dados de um usuário buscando pelo CPF."""
    print("\n--- Atualizar Usuário ---")
    cpf_busca = input("Digite o CPF do usuário que deseja atualizar (apenas números): ")
    cpf_busca = ''.join(filter(str.isdigit, cpf_busca))
    
    for u in usuarios:
        if u.get('cpf') == cpf_busca:
            print(f"Usuário encontrado: {u['nome']}")
            print("Pressione Enter para manter o valor atual.")
            
            novo_nome = input(f"Novo nome ({u['nome']}): ")
            novo_email = input(f"Novo email ({u['email']}): ")
            
            # Se o usuário não digitar nada, mantém o original
            u['nome'] = novo_nome if novo_nome.strip() else u['nome']
            u['email'] = novo_email if novo_email.strip() else u['email']
            
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso!")
            return
            
    print("Usuário não encontrado com esse CPF.")

def deletar_usuario(usuarios):
    """(D)elete: Remove um usuário buscando pelo CPF."""
    print("\n--- Deletar Usuário ---")
    cpf_busca = input("Digite o CPF do usuário que deseja deletar (apenas números): ")
    cpf_busca = ''.join(filter(str.isdigit, cpf_busca))
    
    for i, u in enumerate(usuarios):
        if u.get('cpf') == cpf_busca:
            print(f"Deletando o registro de: {u['nome']}...")
            usuarios.pop(i)
            salvar_usuarios(usuarios)
            print("Usuário deletado com sucesso!")
            return
            
    print("Usuário não encontrado com esse CPF.")

def menu():
    """Função principal para controlar o fluxo do programa."""
    usuarios = carregar_usuarios()
    
    while True:
        print("\n" + "="*30)
        print("       SISTEMA CRUD")
        print("="*30)
        print("1. Cadastrar Usuário (Create)")
        print("2. Listar Usuários   (Read)")
        print("3. Atualizar Usuário (Update)")
        print("4. Deletar Usuário   (Delete)")
        print("5. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios)
        elif opcao == '5':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
