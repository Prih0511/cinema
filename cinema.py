#pedir quantidade de acentos para usuario.
quant_acento = int(input("Quantos acentos deseja em seu cinema(múltiplos de 10)?"))
#escrever abc / dicionario
abc = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
#add 1 ao total do calculo. para nao usar o 0 no inicio do loop for de impresao. evitando calcular o resto 10/0.
lista_cadeira = [" _ "] * (quant_acento + 1)
#while que para o programa depois de tudo ocupado.
# lista_cadeira [1: ] para começar do 1 e nao do 0 como estava antes.
while " _ " in lista_cadeira [1: ]:

    print (" A  B  C  D  E  F  G  H  I  J")
#no intevalo entre 1 até o len da lista_cadeira escreve " _ " pulando uma linha a cade 10.
    for indice in range(1, len(lista_cadeira)):
        print (lista_cadeira[indice] , end = '' )
        if ( indice % 10 == 0 ):
            numero_lateral = (indice / 10)
            print("%1.0f" %numero_lateral)
#pergunta ao usuario sobre acentos
    coluna = input("\n\nDigite a COLUNA:")
#coluna.upper muda tudo para maiusculo/.strip tira todos os espaços para nao dar erro.
    coluna = coluna.upper().strip()
    fila = int(input("Digite a FILA:"))
#conta das cadeiras / x acentos reservados
    acento_escolhido = (fila * 10 + abc[coluna] ) - 10
#fazer cadeira ocupada / \t para deixar no meio fica fofinho
    if lista_cadeira[acento_escolhido] == " x ":
        print ("\n\t **Acento ocupado, escolha outro.**")
    else:
        lista_cadeira[acento_escolhido] = " x "
# termino do loop / ultimos avisos       
print ("\ntodos os acentos ocupados.")
print ("\nPreparem sua pipoca, vamos começar o filme!\n")
print ("Obrigada pela preferencia.")

# fim do programa. Obrigada Professor!!!
