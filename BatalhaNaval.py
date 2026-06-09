import random
 
#tabuleiros

tabuleiro = [ [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

tjogador = [  [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

jfeedback = [ [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

tcomputador = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
              ]

cfeedback = [  [0,0,0,0,0,0,0,0,0,0],
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


t2jogador = [ [0,0,0,0,0,0,0,0,0,0],
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

j2feedback = [[0,0,0,0,0,0,0,0,0,0],
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

t2computador =[[0,0,0,0,0,0,0,0,0,0],
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

c2feedback =[  [0,0,0,0,0,0,0,0,0,0],
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
#contadores
quantidade_embarcaçoes = [5, 5]

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
        print("          TABULEIRO")
        for i in range(len(tabuleiro)):
            print(tabuleiro[i])
            
    elif modo == 2:
        print("          TABULEIRO")
        for i in range(len(tabuleiro2)):
            print(tabuleiro2[i])

    # Seleção das jogadas:
    if modo == 1:
        for i in range(5):
            Linha = int(input("Digite a linha em que você quer jogar: 1-5: "))
            while Linha < 1 or Linha > 5:
                Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-5: "))

            Coluna = int(input("Digite a coluna em que você quer jogar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))
            print()

            tjogador[Linha - 1][Coluna - 1] = "B"
        for i in range(5):
            Linha = random.randint(1,5)
            Coluna = random.randint(1,5)
            tcomputador[Linha - 1][Coluna - 1] = "B"
        return 1
        
    elif modo == 2:
        for i in range(5):
            Linha = int(input("Digite a linha em que você quer jogar: 1-10: "))
            while Linha < 1 or Linha > 10:
                 Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-10: "))

            Coluna = int(input("Digite a coluna em que você quer jogar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))
            print()

            t2jogador[Linha - 1][Coluna - 1] = "B"
        for i in range(5):
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            t2computador[Linha - 1][Coluna - 1] = "B"
        return 2
        # for i in range(len(t2computador)):
        #     print(t2computador[i])
    
        

#Fazendo o ataque
def ataquej(modo):
    if modo == 1:
        for i in range(len(tabuleiro)):
            print(tabuleiro[i])
        Linha = int(input("Digite a linha que você quer atacar: 1-5: "))
        while Linha < 1 or Linha > 10:
                 Linha = int(input("Digite CORRETAMENTE a linha que você quer atacar: 1-5: "))

        Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
        while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))
        print()
        if tcomputador[Linha - 1][Coluna - 1] == "B":
            return True
        else:
            return False
    if modo == 2:
        for i in range(len(tabuleiro2)):
            print(tabuleiro[i])
        Linha = int(input("Digite a linha que você quer atacar: 1-10: "))
        while Linha < 1 or Linha > 10:
                 Linha = int(input("Digite CORRETAMENTE a linha que você quer atacar: 1-10: "))

        Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
        while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))
        print()
        if t2computador[Linha - 1][Coluna - 1] == "B":
            return True
        else:
            return False

#Fazendo o ataque do pc
def ataquec(modo):
     if modo == 1:
          for i in range(len(tabuleiro)):
            Linha = random.randint(1,5)
            Coluna = random.randint(1,10)
            if tcomputador[Linha - 1][Coluna - 1] == "B":
                return True
            else:
                 return False
     if modo == 2:
          for i in range(len(tabuleiro2)):
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            if tcomputador[Linha - 1][Coluna - 1] == "B":
                tabuleiro2[Linha - 1][Coluna - 1] == "X"
                return True
            else:
                 tabuleiro2[Linha - 1][Coluna - 1] == "N"
                 return False

# Rodada
def rodada(modo):
     if modo == 1:
        for linha in range(len(tabuleiro)):
            print(tabuleiro[linha])          
        if ataquej(modo) == True:
            print("Fogo! Você acertou!\nVez do computador:")
            quantidade_embarcaçoes[0] -= 1
        else:
            print("Água! Você errou.\nVez do computador:")
        if ataquec(modo) == True:
            print("Fogo! O computador acertou!\nSua vez:")
            quantidade_embarcaçoes[1] -= 1
        else:
            print("Água! O computador errou.\nSua vez:")
        if quantidade_embarcaçoes[0] != 0 or quantidade_embarcaçoes[1] != 0:
            rodada(modo)


rodada(selecao(menu()))

# #Mostrando o tabuleiro de feedback
# def feedback():

# #verificando a vitoria
# def verificacao():
# fazer a rodada (mostrar feedback, fazer ataque, verificar, e repetir pro adversário)