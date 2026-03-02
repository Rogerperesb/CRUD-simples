# Sistema de Cadastro CRUD em Python

Um sistema de gerenciamento de usuários (CRUD - Create, Read, Update, Delete) desenvolvido em Python rodando diretamente no terminal, com funcionalidade integrada de validação de CPF real.

## 🚀 Funcionalidades

- **Create (Cadastrar):** Adiciona novos usuários validando o CPF informado (evitando CPFs inválidos ou duplicados).
- **Read (Listar):** Exibe todos os usuários cadastrados.
- **Update (Atualizar):** Permite buscar um usuário específico pelo CPF e atualizar seu nome ou e-mail de forma fácil.
- **Delete (Deletar):** Permite remover o registro de um usuário através do seu CPF.
- **Armazenamento de Dados:** Utiliza um arquivo local chamado `usuarios.json` para manter os dados persistentes mesmo após fechar a aplicação.

## 📋 Pré-requisitos

Para rodar este projeto, você precisa ter o [Python 3](https://www.python.org/downloads/) instalado na sua máquina.

Você também precisará instalar a biblioteca `validate-docbr`, que é utilizada para realizar a validação matemática e de formato completo dos CPFs no Brasil.

```bash
pip install validate-docbr
```

*(Caso você esteja usando um ambiente virtual, certifique-se de ativá-lo antes de instalar a dependência).*

## ⚙️ Como executar

1. Clone ou baixe este projeto para a sua máquina local.
2. Abra um terminal na pasta do projeto.
3. Se desejar, ative seu ambiente virtual.
4. Rode o comando abaixo para iniciar o menu interativo:

```bash
python CRUD.py
```

## 📂 Estrutura do Projeto

- `CRUD.py`: É o programa principal contendo a interface em linha de comando, as lógicas do CRUD e a manipulação dos dados com o arquivo `.json`.
- `validarcpf.py`: Um módulo dedicado unicamente a receber um CPF e utilizar o pacote externo para confirmar se ele é válido ou não.
- `usuarios.json`: Arquivo gerado de forma automática na primeira execução que armazena todos os cadastros efetuados. (Ignorado pelo Git, conforme definido no `<.gitignore>`).

---
_Aproveite o sistema! Excelente para iniciar em arquitetura de funções em Python e persistência local de dados._
# CRUD-simples
