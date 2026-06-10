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


tcomputador = [[0,0,0,0,0,0,0,0,0,0],
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
            while tjogador[Linha - 1][Coluna - 1] == "B":
                print("Você já tem um barco aí! Escolha outra posição.")
                Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-5: "))
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))
            tjogador[Linha - 1][Coluna - 1] = "B"

        for i in range(5):
            Linha = random.randint(1,5)
            Coluna = random.randint(1,5)
            while tcomputador[Linha - 1][Coluna -1] == "B":
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

            while t2jogador[Linha - 1][Coluna - 1] == "B":
                print("Você já tem um barco aí! Escolha outra posição.")
                Linha = int(input("Digite CORRETAMENTE a linha em que você quer jogar: 1-10: "))
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer jogar: 1-10: "))    
            print()

            t2jogador[Linha - 1][Coluna - 1] = "B"
        for i in range(5):
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            while t2computador[Linha - 1][Coluna -1] == "B":
                Linha = random.randint(1,5)
                Coluna = random.randint(1,5)
            t2computador[Linha - 1][Coluna - 1] = "B"
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
            Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
                
        print()
        if tcomputador[Linha - 1][Coluna - 1] == "B":
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
            Coluna = int(input("Digite a coluna que você quer atacar: 1-10: "))
        print()
        if t2computador[Linha - 1][Coluna - 1] == "B":
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
        if tjogador[Linha - 1][Coluna - 1] == "B":
                tjogador[Linha - 1][Coluna - 1] = "X"
                return True
        else:
                 tjogador[Linha - 1][Coluna - 1] = "N"
                 return False
     if modo == 2:
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)
            while c2feedback[Linha - 1][Coluna - 1] == "X" or c2feedback[Linha - 1][Coluna - 1] == "N":
                Linha = random.randint(1, 10)
                Coluna = random.randint(1, 10)
            print()
            print("Computador atacou LINHA: ",Linha," e COLUNA: ",Coluna)
            print()
            if t2jogador[Linha - 1][Coluna - 1] == "B":
                c2feedback[Linha - 1][Coluna - 1] = "X"
                return True
            else:
                 c2feedback[Linha - 1][Coluna - 1] = "N"
                 return False

#verificando a vitoria
def verificacao():
    if quantidade_embarcaçoes[0] == 0:
        print("O computador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique E Davi")
        return True

    if quantidade_embarcaçoes[1] == 0:
        print("Jogador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique E Davi")
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
            print(tjogador[linha])    
        print("--------------------------------")
        print("          TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(computadorfeedback)):
            print(tabuleiro[linha])
            
        #Rodada do jogador
        if ataque_jogador(modo) == True:
            while ataque_jogador(modo) == True:
                print("Fogo! Você acertou!\n Jogue novamente: ")
                quantidade_embarcaçoes[0] -= 1
                ataque_jogador(modo)
        else:
            print("Água! Você errou.\nVez do computador:")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!\nComputador novamente")
            quantidade_embarcaçoes[1] -= 1
            ataque_computador(modo)
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
        print("--------------------------------")
        print("          TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(c2feedback)):
            print(c2feedback[linha])
        #Rodada do jogador
        if ataque_jogador(modo) == True:
            print("Fogo! Você acertou!\n Jogue novamente: ")
            quantidade_embarcaçoes[0] -= 1
            ataque_jogador(modo)
        else:
            print("Água! Você errou.\nVez do computador:")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!\nComputador novamente:")
            quantidade_embarcaçoes[1] -= 1
            ataque_computador(modo)
        else:
            print("Água! O computador errou.\nSua vez:")
        if not verificacao():
            rodada(modo)
         
         


rodada(selecao(menu()))

