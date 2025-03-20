def exibir_menu():
    print("Bem vindo ao menu Cadastro!")
    print("1 - Novo cadastro")
    print("2 - Ver casdastro")
    print("3 - Sair")
    print("---------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    turma = input("Digite sua turma:")
    curso = input("Digite seu curso:")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros (cadastros):
    if not cadastros:
        print("\n Nenhum cadastro no sistema")
    else:
        print("\n--------lista de cadastro--------")

        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa ['Nome']}, Idade: {pessoa['Idade']}, Turma:{pessoa['Turma']}, Curso:{pessoa['Curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastros(cadastros)
        
        elif opção == "3":
            print("Obrigada por utilizar nosso sistema")
            break
    
        else:
            print("Opção incorreta, tente novamente")
        
        
if __name__== "__main__":
    main()

