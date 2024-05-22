#criação de variaveis globais
produto1 = 30
produto2 = 50
produto3 = 400
codigo10 = "desconto10"
codigo20 = "desconto20"
codigo30 = "desconto30"
compra_final = 0

#criação das funções dos descontos aplicados

def desconto10(opcao,produto1,produto2,produto3):
    global compra_final
    if opcao == "produto 1":
        compra_final = produto1 - produto1*0.10
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 2":
        compra_final = produto2 - produto2*0.10
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 3":
        compra_final = produto3 - produto3*0.10
        print("preço total da compra: ",compra_final)
    else:
        print("produto não identificado")
def desconto20(opcao,produto1,produto2,produto3):
    global compra_final
    if opcao == "produto 1":
        compra_final = produto1 - produto1*0.20
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 2":
        compra_final = produto2 - produto2*0.20
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 3":
        compra_final = produto3 - produto3*0.20
        print("preço total da compra: ",compra_final)
    else:
        print("produto não identificado")
def desconto30(opcao,produto1,produto2,produto3):
    global compra_final
    if opcao == "produto 1":
        compra_final = produto1 - produto1*0.30
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 2":
        compra_final = produto2 - produto2*0.30
        print("preço total da compra: ",compra_final)
    elif opcao == "produto 3":
        compra_final = produto3 - produto3*0.30
        print("preço total da compra: ",compra_final)
    else:
        print("produto não identificado")


#sistema da loja em looping
comprar = True

while comprar == True:
    print("produto 1 - ",produto1,"R$ ","produto 2 - ",produto2,"R$ ","produto 3 - ",produto3,"R$")
    opcao = str(input("insira o produto que deseja comprar: "))
    if opcao == "produto 1" or opcao == "produto 2" or opcao == "produto3":
        desconto = str(input("possui código de desconto? "))
        if desconto == "sim":
            codigo_desconto = str(input("digite o código de desconto: "))
            if codigo_desconto == codigo10:
                print("código válidado")
                desconto10(opcao,produto1,produto2,produto3)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
            elif codigo_desconto == codigo20:
                print("código válidado")
                desconto20(opcao,produto1,produto2,produto3)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
            elif codigo_desconto == codigo30:
                print("código válidado")
                desconto30(opcao,produto1,produto2,produto3)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
            else:
                print("código inválido")
        else:
            if opcao == "produto 1":
                print("preço total da compra é: ", produto1)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
            elif opcao == "produto 2":
                print("preço total da compra é: ",produto2)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
            elif opcao == "produto 3":
                print("preço total da compra é: ", produto3)
                finalizar = str(input("deseja finalizar a compra? "))
                if finalizar == "sim":
                    print("compra finalizada ")
                else:
                    print("compra cancelada")
    else:
        print("produto não identificado")
    continuar = str(input("deseja continuar fazendo compras? "))
    if continuar == "sim":
        comprar == True
    else:
        comprar = False
        print("programa encerrado")
