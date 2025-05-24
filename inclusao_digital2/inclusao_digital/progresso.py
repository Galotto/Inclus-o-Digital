import json
import os

ARQUIVO = "dados/progresso.json"

# Garante que a pasta e o arquivo existam
os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=4)

# Lê o arquivo de progresso dos alunos e retorna os dados em formato de dicionário.
def carregar_progresso():
    if not os.path.exists(ARQUIVO):
        return {}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return {}
        return json.loads(conteudo)

# Salva no disco os dados de progresso dos alunos em um arquivo JSON.
def salvar_progresso(progresso: dict) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(progresso, f, indent=4, ensure_ascii=False)

# Atualiza o progresso de um aluno específico, somando novos acertos e respostas.
def atualizar_progresso(email: str, acertos: int, total: int) -> None:
    progresso = carregar_progresso()
    if email not in progresso:
        progresso[email] = {"acertos": 0, "total": 0}
    progresso[email]["acertos"] += acertos
    progresso[email]["total"] += total
    salvar_progresso(progresso)
