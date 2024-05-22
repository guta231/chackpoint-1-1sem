#variaveis globais
sua_conta = 300
fernanda = 0
mateus = 0
gustavo = 0
print("sua conta - ",sua_conta,"R$"," fernanda - ",fernanda, "R$"," mateus - ",mateus,"R$"," gustavo - ", gustavo,"R$")

#função para a transferencia
def transferencia(sua_conta,fernanda,mateus,gustavo):
    opcao = True
    while opcao == True:

        conta = int(input("para qual conta deseja tranferir? para fernanda - 1 / mateus - 2 / gustavo - 3: "))
        valor = float(input("insira o valor que deseja transferir: "))
        if conta == 1 and valor <= sua_conta and valor > 0:
            sua_conta = sua_conta - valor
            fernanda = fernanda + valor
            print("transferencia realizada")
            print("sua conta - ",sua_conta,"R$"," fernanda - ",fernanda, "R$"," mateus - ",mateus,"R$"," gustavo - ", gustavo,"R$")
        elif conta == 2 and valor <= sua_conta and valor > 0:
            sua_conta = sua_conta - valor
            mateus = mateus + valor
            print("transferencia realizada")
            print("sua conta - ",sua_conta,"R$"," fernanda - ",fernanda, "R$"," mateus - ",mateus,"R$"," gustavo - ", gustavo,"R$")
        elif conta == 3 and valor <= sua_conta and valor > 0:
            sua_conta = sua_conta - valor
            gustavo = gustavo + valor
            print("transferencia realizada")
            print("sua conta - ",sua_conta,"R$"," fernanda - ",fernanda, "R$"," mateus - ",mateus,"R$"," gustavo - ", gustavo,"R$")
        elif valor > sua_conta or valor <= 0:
            print("valor de transferência inválido")
        else:
            print("conta inválida")
        pergunta = str(input("deseja continuar fazendo transferencias?"))
        if pergunta == "sim":
            opcao = True
        elif pergunta == "não" or pergunta == "nao":
            print("Programa encerrado")
            opcao = False
#chamando a função ao inicializar o programa
transferencia(sua_conta,fernanda,mateus,gustavo)