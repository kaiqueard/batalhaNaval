import random
 
#tabuleiros

tabuleiro = [ [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

toculto = [   [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

tabuleiro2 = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
]


t2culto = [  [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
]

#Tamanho do Tabuleiro
def menu():
    
    modo = int(input(
        "Digite o número equivalente a sua jogada: " \
    "\n1 - Tabuleiro 5x10"
    "\n2 - Tabuleiro 10x10" \
    "\n"
    ))
    if modo!=2 and modo!=1:
        print("Digite corretamente!")
        menu()
    else:
        return modo


#Mostrando o Tabuleiro
def selecao(modo):
    if modo == 1:
        for i in range(len(tabuleiro)):
            print(tabuleiro[i])
            
    elif modo == 2:
        for i in range(len(tabuleiro2)):
            print(tabuleiro2[i])

    # Seleção das jogadas:
    if modo == 1:
        for i in range(5):
            Linha = int(input("Digite a linha em que você quer jogar: 1-5: "))
            Coluna = int(input("Digite a coluna em que você quer jogar: 1-10: "))
            print()
            toculto[Linha - 1][Coluna - 1] = "X"
        for i in range(len(toculto)):
            print(toculto[i])
    elif modo == 2:
        for i in range(5):
            Linha = int(input("Digite a linha em que você quer jogar: 1-5: "))
            Coluna = int(input("Digite a coluna em que você quer jogar: 1-10: "))
            print()
            t2culto[Linha - 1][Coluna - 1] = "X"
        for i in range(len(t2culto)):
            print(t2culto[i])


selecao(menu())

