import random
 
#tabuleiros

tabuleiro = [ [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              ]

tabuleiro_jogador = [  [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
]


tabuleiro_computador = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
              ]

computadorfeedback = [  [0,0,0,0,0,0,0,0,0,0],
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


tabuleiro2jogador = [ [0,0,0,0,0,0,0,0,0,0],
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


tabuleiro2computador =[[0,0,0,0,0,0,0,0,0,0],
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

computador2feedback =[ [0,0,0,0,0,0,0,0,0,0],
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
        return menu()
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
            while tabuleiro_jogador[Linha - 1][Coluna - 1] == "B":
                print("Você já tem um barco aí! Escolha outra posição.")
                Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-5: "))
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))
            tabuleiro_jogador[Linha - 1][Coluna - 1] = "B"

        for i in range(5):
            Linha = random.randint(1,5)
            Coluna = random.randint(1,5)
            while tabuleiro_computador[Linha - 1][Coluna -1] == "B":
                Linha = random.randint(1,5)
                Coluna = random.randint(1,5)
            tabuleiro_computador[Linha - 1][Coluna - 1] = "B"
        return 1
        
    elif modo == 2:
        for i in range(5):
            Linha = int(input("Digite a linha em que você quer jogar: 1-10: "))
            while Linha < 1 or Linha > 10:
                 Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-10: "))

            Coluna = int(input("Digite a coluna em que você quer jogar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))

            while tabuleiro2jogador[Linha - 1][Coluna - 1] == "B":
                print("Você já tem um barco aí! Escolha outra posição.")
                Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-10: "))
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))    
            print()

            tabuleiro2jogador[Linha - 1][Coluna - 1] = "B"
        for i in range(5):
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            while tabuleiro2computador[Linha - 1][Coluna -1] == "B":
                Linha = random.randint(1,5)
                Coluna = random.randint(1,5)
            tabuleiro2computador[Linha - 1][Coluna - 1] = "B"
        return 2
        # for i in range(len(t2computador)):
        #     print(t2computador[i])
    
        

#Fazendo o ataque
def ataque_jogador(modo):
    if modo == 1:
        Linha = int(input("Digite a linha que você quer atacar: 1-5: "))
        while Linha < 1 or Linha > 5:
                 Linha = int(input("Digite CORRETAMENTE a linha que você quer atacar: 1-5: "))
                 
        print()
        Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
        while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))
        
        while tabuleiro[Linha - 1][Coluna - 1] == "X" or tabuleiro[Linha - 1][Coluna - 1] == "N":
            print("Você já atacou essa posição! Escolha outra.")
            Linha = int(input("Digite a linha que você quer atacar: 1-5: "))
            while Linha < 1 or Linha > 5:
                Linha = int(input("Digite CORRETAMENTE a linha que você quer atacar: 1-5: "))

            Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                 Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))
                
        print()
        if tabuleiro_computador[Linha - 1][Coluna - 1] == "B":
            tabuleiro[Linha - 1][Coluna - 1] = "X"
            return True
        else:
            tabuleiro[Linha - 1][Coluna - 1] = "N"
            return False
    if modo == 2:
        Linha = int(input("Digite a linha que você quer atacar: 1-10: "))
        while Linha < 1 or Linha > 10:
                 Linha = int(input("Digite CORRETAMENTE a linha que você quer atacar: 1-10: "))

        Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
        while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))

        while tabuleiro2[Linha - 1][Coluna - 1] == "X" or tabuleiro2[Linha - 1][Coluna - 1] == "N":
            print("Você já atacou essa posição! Escolha outra.")
            Linha = int(input("Digite a linha que você quer atacar: 1-10: "))
            while Linha < 1 or Linha > 10:
                Linha = int(input("Digite a linha que você quer atacar: 1-10: "))

            Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                 Coluna = int(input("Digite CORRETAMENTE a coluna que você quer atacar: 1-10: "))
        print()

        if tabuleiro2computador[Linha - 1][Coluna - 1] == "B":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            return True
        else:
            tabuleiro2[Linha - 1][Coluna - 1] = "N"
            return False

#Fazendo o ataque do pc
def ataque_computador(modo):
     if modo == 1:
        Linha = random.randint(1,5)
        Coluna = random.randint(1,10)
        while computadorfeedback[Linha - 1][Coluna - 1] == "X" or computadorfeedback[Linha - 1][Coluna - 1] == "N":
            Linha = random.randint(1, 5)
            Coluna = random.randint(1, 10)
        print()
        print("Computador atacou LINHA: ", Linha," e COLUNA: ",Coluna)
        print()
        if tabuleiro_jogador[Linha - 1][Coluna - 1] == "B":
                computadorfeedback[Linha - 1][Coluna - 1] = "X"
                return True
        else:
                 computadorfeedback[Linha - 1][Coluna - 1] = "N"
                 return False
     if modo == 2:
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            while computador2feedback[Linha - 1][Coluna - 1] == "X" or computador2feedback[Linha - 1][Coluna - 1] == "N":
                Linha = random.randint(1, 10)
                Coluna = random.randint(1, 10)
            print()
            print("Computador atacou LINHA: ",Linha," e COLUNA: ",Coluna)
            print()
            if tabuleiro2jogador[Linha - 1][Coluna - 1] == "B":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                return True
            else:
                 computador2feedback[Linha - 1][Coluna - 1] = "N"
                 return False

#verificando a vitoria
def verificacao():
    if quantidade_embarcaçoes[0] == 0:
        print("O computador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique & Davi")
        return True

    if quantidade_embarcaçoes[1] == 0:
        print("Jogador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique & Davi")
        return True
    else:
        return False

# Rodada
def rodada(modo):
    if modo == 1:
        print("--------------------------------")
        print("          SEU TABULEIRO")
        print("--------------------------------")
        for linha in range(len(tabuleiro)):
            print(tabuleiro[linha])    
        print("Barcos inimigos restantes: ", quantidade_embarcaçoes[1])
        print("--------------------------------")
        print("          TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(computadorfeedback)):
            print(computadorfeedback[linha])
        print("Barcos inimigos restantes: ", quantidade_embarcaçoes[0])
            
        #Rodada do jogador
        if ataque_jogador(modo) == True:
            print("Fogo! Você acertou!\n Vez do computador: ")
            quantidade_embarcaçoes[1] -= 1
            print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])

        else:
            print("Água! Você errou.\nVez do computador:")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!")
            quantidade_embarcaçoes[0] -= 1
            print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
            
        else:
            print("Água! O computador errou.\nSua vez:")
        if not verificacao():
            rodada(modo)

    elif modo == 2:
        print("--------------------------------")
        print("          SEU TABULEIRO")
        print("--------------------------------")
        for linha in range(len(tabuleiro2)):
            print(tabuleiro2[linha])  
        print("barcos inimigos restantes: ", quantidade_embarcaçoes[1])
        print("--------------------------------")
        print("    TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(computador2feedback)):
            print(computador2feedback[linha])
        print("Barcos inimigos restantes: ", quantidade_embarcaçoes[0])
        #Rodada do jogador
        if ataque_jogador(modo) == True:
            print("Fogo! Você acertou!\n Vez do computador: ")
            quantidade_embarcaçoes[1] -= 1
            print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])
            
        else:
            print("Água! Você errou.\nVez do computador:")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!")
            quantidade_embarcaçoes[0] -= 1
            print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
                
        else:
            print("Água! O computador errou.\nSua vez:")
        if not verificacao():
            rodada(modo)
         
         


rodada(selecao(menu()))

