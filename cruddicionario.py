contatos = {}

while True:

    print(''' 
1. Adicionar contato
2. Listar contatos
3. Atualizar contato
4. Remover contato
5. Sair
    ''')

    opcao = int(input("Escolha sua opção: "))

    if opcao == 1:
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")
        contatos[nome] = {"telefone": telefone, "email": email}
    
    elif opcao == 2:
        if contatos:
            for nome, info in contatos.items():
                print(f''' 
        Nome: {nome}
        Telefone: {info['telefone']}
        Email: {info['email']}''')

        else:
            print("Nenhum contato cadastrado")

    elif opcao == 3:
        nome = input("Digite o nome do contato que deseja atualizar: ")
        if nome in contatos:
            telefone = input("Digite o novo telefone: ")
            email = input("Digite o novo email: ")
            contatos[nome]  = {"telefone": telefone, "email": email}
            print("Contato atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    elif opcao == 4:
        nome = input("Qual contato deseja remover: ")
        if nome in contatos:
            del contatos[nome]
            print("Contato removido")
        else:
            print("Contato não encontrado!")

    elif opcao == 5:
        print("Saindo...")
        break

    else:
        print("Opção Inválida. Tente novamente.")