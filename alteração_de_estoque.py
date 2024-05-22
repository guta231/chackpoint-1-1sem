#variaveis globais
jogo1 = 4
jogo2 = 2
jogo3 = 5
jogo4 = 10

#funções de cada compra de jogo
def opcao1():
    global jogo1
    quantidade = int(input("digite a quantidade do produto que deseja comprar: "))
    if jogo1 > 0 and jogo1 >= quantidade and quantidade > 0:
        jogo1 = jogo1 - quantidade
        print("compra realizada com sucesso")
    elif jogo1 == 0:
        print("jogo fora de estoque")
    elif quantidade > jogo1:
        print("quantidade de produto fora de estoque")
    else:
         print("número inválido")
def opcao2():
    global jogo2
    quantidade = int(input("digite a quantidade do produto que deseja comprar: "))
    if jogo2 > 0 and jogo2 >= quantidade and quantidade > 0:
        jogo2 = jogo2 - quantidade
        print("compra realizada com sucesso")
    elif jogo2 == 0:
        print("jogo fora de estoque")
    elif quantidade > jogo2:
        print("quantidade de produto fora de estoque")
    else:
         print("número inválido")
def opcao3():
    global jogo3
    quantidade = int(input("digite a quantidade do produto que deseja comprar: "))
    if jogo3 > 0 and jogo3 >= quantidade and quantidade > 0:
        jogo3 = jogo3 - quantidade
        print("compra realizada com sucesso")
    elif jogo3 == 0:
        print("jogo fora de estoque")
    elif quantidade > jogo3:
        print("quantidade de produto fora de estoque")
    else:
         print("número inválido")
def opcao4():
    global jogo4
    quantidade = int(input("digite a quantidade do produto que deseja comprar: "))
    if jogo4 > 0 and jogo4 >= quantidade and quantidade > 0:
        jogo4 = jogo4 - quantidade
        print("compra realizada com sucesso")
    elif jogo4 == 0:
        print("jogo fora de estoque")
    elif quantidade > jogo4:
        print("quantidade de produto fora de estoque")
    else:
         print("número inválido")

#loooping do sistema de compra
comprar = True

while comprar == True:
    print("jogo 1 - ",jogo1,"jogo 2 - ",jogo2,"jogo 3 - ",jogo3,"jogo 4 - ",jogo4)
    opcao = str(input("digite o nome do jogo que queira comprar: "))
    if opcao == "jogo 1":
        opcao1()
    elif opcao == "jogo 2":
            opcao2()
    elif opcao == "jogo 3":
            opcao3()
    elif opcao == "jogo 4":
            opcao4()
    else:
        print("nome de jogo inválido")
    i = str(input("deseja continuar comprando? "))
    if i =="sim":
         comprar = True
    else:
         comprar = False
         print("programa encerrado")
