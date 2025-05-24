import json
import os
import random
from progresso import carregar_progresso, atualizar_progresso

ARQUIVO_CURSOS = "dados/cursos.json"

os.makedirs(os.path.dirname(ARQUIVO_CURSOS), exist_ok=True)
if not os.path.exists(ARQUIVO_CURSOS):
    with open(ARQUIVO_CURSOS, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4, ensure_ascii=False)

def carregar_cursos():
    if not os.path.exists(ARQUIVO_CURSOS):
        print("Arquivo de cursos não encontrado.")
        return []

    with open(ARQUIVO_CURSOS, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return []
        return json.loads(conteudo)

def iniciar_curso(usuario):
    email = usuario["email"]

    cursos = carregar_cursos()
    if not cursos:
        print("Nenhuma aula disponível no momento.")
        return

    print("\n=== Início do Curso: Lógica Computacional ===")

    acertos = 0
    total = 0

    random.shuffle(cursos)

    for aula in cursos:
        print(f"\n🧠 {aula['titulo']}")
        print(aula['conteudo'])

        questoes = aula.get("questoes", [
            {
                "pergunta": aula.get("pergunta", ""),
                "alternativas": ["a", "b", "c", "d"],
                "resposta_correta": aula.get("resposta_correta", "")
            }
        ])

        random.shuffle(questoes)

        for q in questoes:
            alternativas = q["alternativas"][:]
            random.shuffle(alternativas)
            print(f"\n{q['pergunta']}")
            for i, alt in enumerate(alternativas):
                print(f"{i + 1}. {alt}")

            try:
                resposta_num = int(input("Escolha a opção correta (1-4): ").strip())
                if 1 <= resposta_num <= len(alternativas):
                    resposta = alternativas[resposta_num - 1]
                else:
                    print("❌ Opção inválida, questão pulada.")
                    total += 1
                    continue
            except ValueError:
                print("❌ Entrada inválida, questão pulada.")
                total += 1
                continue

            if resposta.lower() == q["resposta_correta"].lower():
                print("✔️ Resposta correta!")
                acertos += 1
            else:
                print(f"❌ Resposta incorreta. Resposta correta: {q['resposta_correta']}")
            total += 1

    # Atualiza e salva o progresso usando a função do progresso.py
    atualizar_progresso(email, acertos, total)

    print(f"\n📊 Seu desempenho neste curso: {acertos}/{total} acertos.")

    
