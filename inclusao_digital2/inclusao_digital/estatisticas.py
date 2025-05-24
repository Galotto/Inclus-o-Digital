import json
import os
import subprocess
import sys
from tabulate import tabulate

# Instala automaticamente uma biblioteca, se não estiver instalada
def instalar_se_necessario(pacote):
    try:
        __import__(pacote)
    except ImportError:
        print(f"🔄 Instalando biblioteca '{pacote}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# Garantir que 'tabulate' esteja instalado
instalar_se_necessario("tabulate")

ARQUIVO_PROGRESSO = "dados/progresso.json"
ARQUIVO_USUARIOS = "dados/usuarios.json"

# Carrega os dados de progresso dos alunos a partir do arquivo JSON.
def carregar_progresso():
    if not os.path.exists(ARQUIVO_PROGRESSO):
        return {}
    
    with open(ARQUIVO_PROGRESSO, "r") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return {}
        return json.loads(conteudo)

# Carrega os dados dos usuários a partir do arquivo JSON.
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    
    with open(ARQUIVO_USUARIOS, "r") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return []
        return json.loads(conteudo)

# Função para exibir estatísticas de desempenho dos alunos
def exibir_estatisticas():
    progresso = carregar_progresso()
    usuarios = carregar_usuarios()

    if not progresso:
        print("Nenhum dado de progresso encontrado.")
        return

    print("\n📈 Estatísticas de Desempenho dos Alunos:")

    tabela = []
    totais = []

    mapa_emails_nomes = {u["email"]: u["nome"] for u in usuarios}
    mapa_emails_logins = {u["email"]: u.get("logins", 0) for u in usuarios}

    for email, dados in progresso.items():
        nome = mapa_emails_nomes.get(email, "(Nome não encontrado)")
        logins = mapa_emails_logins.get(email, 0)
        acertos = dados.get("acertos", 0)
        total = dados.get("total", 1)
        porcentagem = round((acertos / total) * 100, 2)
        tabela.append([nome, email, logins, acertos, total, f"{porcentagem}%"])
        totais.append(porcentagem)

    print(tabulate(tabela, headers=["Nome", "Email", "Logins", "Acertos", "Total", "Desempenho"], tablefmt="grid"))

    media_geral = round(sum(totais) / len(totais), 2)
    print(f"\n📌 Média geral de desempenho dos alunos: {media_geral}%")

# Função para exibir estatísticas de um único usuário logado
def exibir_estatisticas_do_usuario(usuario):
    progresso = carregar_progresso()
    email = usuario["email"]

    if email not in progresso:
        print("📭 Nenhum progresso registrado para este usuário.")
        return

    dados = progresso[email]
    acertos = dados.get("acertos", 0)
    total = dados.get("total", 1)
    desempenho = round((acertos / total) * 100, 2)
    logins = usuario.get("logins", 0)

    print("\n📊 Estatísticas do seu desempenho:")
    print(f"Nome: {usuario['nome']}")
    print(f"E-mail: {email}")
    print(f"Logins: {logins}")
    print(f"Acertos: {acertos}")
    print(f"Total de questões: {total}")
    print(f"Desempenho: {desempenho}%")
