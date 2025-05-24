# Ler e escrever arquivos no formato JSON.
import json
# Verificar se o arquivo já existe.
import os
# Criptografar a senha do usuário com SHA-256 (boa prática de segurança).
import hashlib
# Importar o módulo sys para obter o diretório atual do script.
import sys

from seguranca import validar_senha_forte

# Define um diretório fixo para armazenar os dados do sistema, independente do local do .exe
ARQUIVO_USUARIOS = "dados/usuarios.json"

# Garante que a pasta e o arquivo existam
os.makedirs(os.path.dirname(ARQUIVO_USUARIOS), exist_ok=True)
if not os.path.exists(ARQUIVO_USUARIOS):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump([], f, indent=4)

# Verifica se o diretório existe, caso contrário, cria
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []

    with open(ARQUIVO_USUARIOS, "r") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return []
        return json.loads(conteudo)

# Cria o arquivo de usuários se não existir
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

# Função para criar um hash da senha
def hash_senha(senha):
    # Usando SHA-256 para hash da senha
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")

    usuarios = carregar_usuarios()
    if any(u['email'] == email for u in usuarios):
        print("❌ Email já cadastrado.")
        return

    # Loop até o usuário digitar uma senha válida
    while True:
        senha = input("Senha: ")

        if validar_senha_forte(senha):
            break  # Sai do loop se for uma senha forte

        print("\n❌ Senha fraca! A senha deve conter:")
        print("- Pelo menos 6 caracteres")
        print("- Pelo menos uma letra minúscula")
        print("- Pelo menos uma letra maiúscula")
        print("- Pelo menos um número")
        print("Por favor, tente novamente.\n")

    senha_hash = hash_senha(senha)

    usuarios.append({
        "nome": nome,
        "email": email,
        "senha": senha_hash,
        "tipo": "aluno"
    })
    salvar_usuarios(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    email = input("Email: ")
    senha = input("Senha: ")
    senha_hash = hash_senha(senha)

    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['email'] == email and u['senha'] == senha_hash:
            print(f"Bem-vindo(a), {u['nome']}!")

            if "logins" not in u:
                u["logins"] = 0

            u["logins"] += 1
            salvar_usuarios(usuarios)
            return u

    print("Login inválido.")
    return None
