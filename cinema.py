#exercicio do cinema / pedir quantidade de acentos para usuario.
quant_acento = int(input("Quantos acentos deseja em seu cinema(múltiplos de 10)?"))
#escrever abc / dicionario
abc = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
#arrumar os acentos _ vagos.
#add 1 ao total do calculo. para nao usar o 0 no inicio do loop for de impresao. evitando calcular o resto 10/0.
lista_cadeira = [" _ "] * (quant_acento + 1)
#começo do loop
while True:
    print (" A  B  C  D  E  F  G  H  I  J")
    for indice in range(1, len(lista_cadeira)):
        print (lista_cadeira[indice] , end = '' )
        if ( indice % 10 == 0 ):
            numero_lateral = (indice / 10)
            print("%1.0f" %numero_lateral)
    #pergunta ao usuario sobre acentos
    coluna = input("\n\nDigite a COLUNA:")
    coluna = coluna.upper().strip()
    fila = int(input("Digite a FILA:"))
    #conta das cadeiras / x acentos reservados
    acento_escolhido = (fila * 10 + abc[coluna] ) - 10
    lista_cadeira[acento_escolhido] = " x "
    #fazer cadeira ocupada
    if lista_cadeira[acento_escolhido] == " x ":
        print ("acento ocupado, escolha outro.")
    #ops. digitou algo errado digite novamente.
    #elif coluna == int:
       # print ("Ops. digitou algo errado tente novamente.")
    #elif fila == " ":
       # print ("Ops. digitou algo errado tente novamente.")
    
#fazer 0 para fechar

#agradecer ao usuario
#arrumar os numeros depois do 01
#fazer cadeira ocupada


#todos os lugares ocupados, vamos comecar a sessao.
#preparem sua pipoca!
#com problema no abc
#com problema com a coluna a e a fila 1

   




