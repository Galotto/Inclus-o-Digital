from usuarios import cadastrar_usuario, login
from cursos import iniciar_curso
from estatisticas import exibir_estatisticas, exibir_estatisticas_do_usuario

# Menu exibido após o login do usuário
def menu_pos_login(usuario):
    while True:
        print(f"\nBem-vindo(a), {usuario['nome']}!\n")
        print("1. Responder questionário")
        print("2. Ver minhas estatísticas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_curso(usuario)
        elif opcao == "2":
            exibir_estatisticas_do_usuario(usuario)
        elif opcao == "3":
            print("Saindo da sessão...")
            break
        else:
            print("Opção inválida.")

# É um sistema de gerenciamento de usuários para um sistema de cursos online.
def menu():
    while True:
        # Exibe o menu principal
        print("\n=== Menu Principal ===")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")
        print("4. Ver estatísticas gerais")  # nova linha

        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = login()
            if usuario:
                menu_pos_login(usuario)
        elif opcao == "3":
            print("Saindo...")
            break
        elif opcao == "4":
            exibir_estatisticas()  # nova ação
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

