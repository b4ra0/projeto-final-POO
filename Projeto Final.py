from sys import exit
from time import sleep

# ----------- Começo do código --------------- #

pedido = list()
cliente = dict()
listaDeClientes = list()
valor = 0
menuPrincipal = "s"
print ("Bem vindo à pizzaria do Barão")
sleep(2)
print ("Este é o nosso serviço de pedidos")
sleep(2)
while menuPrincipal == "s":
    print ("Nosso cadápio é dividido em 6 seções")
    print("1- Pizzas tradicionais")
    print("2- Pizzas especiais")
    print("3- Pizzas doces")
    print("4- Bebidas")
    print("5- Carrinho")
    print("6- Dados")
    opcao = int(input("Digite o número da seção para fazer seu pedido "))
    if opcao == 1:
        print("Você escolheu a seção das pizzas tradicionais")
        print("Nossas opções de pizzas tradicionais são: \n4 Queijos \nCalabresa \nPortuguesa \nMussarela \nFrango \nMarguerita \nBacon")
        print("Dentre os tamanhos das pizzas tradicionais temos a Broto (R$19,90), a Média (R$29,90), a Grande (R$39,90) e a Gigante (R$49,90)")
        saborTradicional = str(input("Digite um dos sabores apresentados acima "))
        tamanhoTradicional = str(input("Digite o tamanho da sua pizza "))
        if tamanhoTradicional == "Broto":
            valor += 19.90
        elif tamanhoTradicional == "Média":
            valor += 29.90
        elif tamanhoTradicional == "Grande":
            valor += 39.90
        elif tamanhoTradicional == "Gigante":
            valor += 49.90
        else:
            print("O tamanho da sua pizza é inválido, por favor, refaça seu pedido")
            exit()
        pedido.append(saborTradicional)
        pedido.append(tamanhoTradicional)
        menuPrincipal = str(input("Você deseja voltar ao menu principal? s/n "))
    elif opcao == 2:
        print("Você escolheu a seção das pizzas especiais")
        print("Nossas opções de pizzas especiais são: \nFrango com Cheddar \nVegetariana \nCatuperu \nPepperoni \nFilé Mignon \nStrogonoff")
        print("Dentre os tamanhos das pizzas especiais temos a Broto (R$25,00), a Média (R$35,00), a Grande (R$45,00) e a Gigante (R$55,00)")
        saborEspecial = str(input("Digite um dos sabores apresentados acima "))
        tamanhoEspecial = str(input("Digite o tamanho da sua pizza "))
        if tamanhoEspecial == "Broto":
            valor += 25
        elif tamanhoEspecial == "Média":
            valor += 35
        elif tamanhoEspecial == "Grande":
            valor += 45
        elif tamanhoEspecial == "Gigante":
            valor += 55
        else:
            print("O tamanho da sua pizza é inválido, por favor, refaça seu pedido")
            exit()
        pedido.append(saborEspecial)
        pedido.append(tamanhoEspecial)
        menuPrincipal = str(input("Você deseja voltar ao menu principal? s/n "))
    elif opcao == 3:
        print("Você escolheu a seção das pizzas doces")
        print("Nossas opções de pizzas doces são: \nChocolate Preto \nChocolate Branco \nBanana \nSensação \nPrestígio")
        print("Dentre os tamanhos das pizzas doces temos a Broto (R$23,00), a Média (R$33,00), a Grande (R$43,00) e a Gigante (R$53,00)")
        saborDoce = str(input("Digite um dos sabores apresentados acima "))
        tamanhoDoce = str(input("Digite o tamanho da sua pizza "))
        if tamanhoDoce == "Broto":
            valor += 23
        elif tamanhoDoce == "Média":
            valor += 33
        elif tamanhoDoce == "Grande":
            valor += 43
        elif tamanhoDoce == "Gigante":
            valor += 53
        else:
            print("O tamanho da sua pizza é inválido, por favor, refaça seu pedido")
            exit()
        pedido.append(saborDoce)
        pedido.append(tamanhoDoce)
        menuPrincipal = str(input("Você deseja voltar ao menu principal? s/n "))
    elif opcao == 4:
        print("Você escolheu a seção das bebidas")
        print("Nossas opções de bebidas são: \nRefrigerante \nÁgua \nCerveja")
        tipoBebida = str(input("Digite sua opção de bebida "))
        if tipoBebida == "Refrigerante":
            print("Você escolheu refrigerante")
            print("Nossas opções de refrigerante são: \nCoca Cola \nSprite \nGuaraná \nFanta")
            tipoRefri = str(input("Digite sua opção de refrigerante "))
            pedido.append(tipoRefri)
            valor += 4.5
        elif tipoBebida == "Água":
            print("Você escolheu Água")
            print("Nossas opções de Água são: \nÁgua com Gás \nÁgua sem Gás")
            tipoAgua = str(input("Digite sua opção de refrigerante "))
            pedido.append(tipoAgua)
            valor += 3
        elif tipoBebida == "Cerveja":
            print("Você escolheu cerveja")
            print("Nossas opções de cerveja são: \nHeineken \nOriginal \nSkol \nBrahma \nAmstel")
            tipoCerveja = str(input("Digite sua opção de cerveja "))
            pedido.append(tipoCerveja)
            valor += 5
        menuPrincipal = str(input("Você deseja voltar ao menu principal? s/n "))
    elif opcao == 5:
        print("Você escolheu a seção do carrinho")
        print(pedido)
        print(valor)
        cadastrar = str(input("Você deseja ir para o cadastro? s/n "))
        if cadastrar == "s":
            print("Para finalizar sua compra você terá que fazer um cadastro")
            cliente['Nome'] = str(input("Digite o seu nome "))
            cliente['CPF'] = int(input("Digite o seu CPF "))
            cliente['Endereço'] = str(input("Digite o seu endereço "))
            print("Seu pedido ficou assim", pedido)
            print("O valor ficou de R$", valor)
            finalizarCompra = str(input("Você deseja finalizar o pedido? s/n "))
            if finalizarCompra == "s":
                print("Obrigado por finalizar sua compra, seu pedido já foi recebido pela nossa pizzaria e deverá chegar no seu endereço em, aproximadamente 50 minutos")
                print("Agradecemos a preferência")
                cliente['Valor'] = valor
                cliente['Pedido'] = pedido
                listaDeClientes.append(cliente.copy())
                valor = 0
        menuPrincipal = str(input("Você deseja voltar ao menu principal? s/n "))
    elif opcao == 6:
        print("Você escolheu a seção dados")
        menuDados = "s"
        while menuDados == "s":
            alterarDados = int(input("O que você deseja fazer?\n1- Alterar meu pedido\n2- Excluir pedido\n3- Consultar pedido\n4- Voltar ao Menu Principal "))
            if alterarDados == 1:
                print("Você escolheu alterar seu pedido")
                nomeAlterar = str(input('Digite o seu nome '))
                cliente['Nome'] = nomeAlterar
                dadoAlterar = str(input('Qual dado você deseja alterar? Nome / CPF / Endereço '))
                dadoAlterado = str(input('Insira como você quer que fique '))
                cliente[dadoAlterar] = dadoAlterado
                print('Ficou assim ', cliente)
            elif alterarDados == 2:
                print("Você escolheu excluir seu pedido")
                CPFExcluir = int(input('Digite o seu CPF '))
                cliente['CPF'] = CPFExcluir
                cliente.clear()
                print('Seu pedido foi apagado com sucesso')
            elif alterarDados == 3:
                print("Você escolheu consultar seu pedido")
                CPFConsulta = int(input('Digite o seu CPF '))
                cliente['CPF'] = CPFConsulta
                print(cliente)
            elif alterarDados == 4:
                menuDados = "n"
            else:
                print("Por favor digite um número válido")
    else:
        print("Por favor, digite um número válido")
        sleep(1)