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
#variáveis
quantidade_embarcaçoes = [5, 5]
#variáveis pro desafio
porta_avioes = [5,5]
navio_tanque = [4,4]
contratorpedeiro = [3,3]
submarino = [2,2]
destroier = [1,1]

#Tamanho do Tabuleiro
def menu():
    
    modo = int(input(
        "Bem-vindo(a) ao Batalha Naval"
        "\nDigite o número equivalente a sua jogada: " \
    "\n1 - Tabuleiro 5x10"
    "\n2 - Tabuleiro 10x10" \
    "\n3 - Modo original(10x10 & Regras Especiais)\n"
    ))
    if modo!=2 and modo!=1 and modo!=3:
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
#--------------------------------
#     DESAFIO, modo original
#--------------------------------
    elif modo == 3:
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
#--------------------------------
#     DESAFIO, modo original
#--------------------------------
    elif modo == 3:
        print("!!!ATENÇÂO!!!, siga todas as regras como solicitado para uma experiência mais satisfatória." \
        "\n\nVamos começar com a embarcação 5 e indo de forma decrescente até a 1\n\n"
        "Porta-aviões     - 5 posições\n"
        "Navio-tanque     - 4 posições\n"
        "Contratorpedeiro - 3 posições\n"
        "Submarino        - 2 posições\n"
        "Destroier        - 1 posição")
        for i in range(5):
            selecao_barcos_jogador(i)
        for i in range(5):
            selecao_barcos_pc(i)
        return 3
    
    
    
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
    
    if modo == 3:
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

        if tabuleiro2computador[Linha - 1][Coluna - 1] == "P":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            porta_avioes[1] -= 1
            return True
        elif tabuleiro2computador[Linha - 1][Coluna - 1] == "T":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            navio_tanque[1] -= 1
            return True
        elif tabuleiro2computador[Linha - 1][Coluna - 1] == "C":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            contratorpedeiro[1] -= 1
            return True
        elif tabuleiro2computador[Linha - 1][Coluna - 1] == "S":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            submarino[1] -= 1
            return True
        elif tabuleiro2computador[Linha - 1][Coluna - 1] == "D":
            tabuleiro2[Linha -1][Coluna - 1] = "X"
            destroier[1] -= 1
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
     if modo == 3:
        Linha = random.randint(1,10)
        Coluna = random.randint(1,10)
        while computador2feedback[Linha - 1][Coluna - 1] == "X" or computador2feedback[Linha - 1][Coluna - 1] == "N":
            Linha = random.randint(1, 10)
            Coluna = random.randint(1, 10)
            print()
            print("Computador atacou LINHA: ",Linha," e COLUNA: ",Coluna)
            print()
            if tabuleiro2jogador[Linha - 1][Coluna - 1] == "P":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                porta_avioes[0] -= 1
                return True
            elif tabuleiro2jogador[Linha - 1][Coluna - 1] == "T":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                navio_tanque[0] -= 1
                return True
            elif tabuleiro2jogador[Linha - 1][Coluna - 1] == "C":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                contratorpedeiro[0] -= 1
                return True
            elif tabuleiro2jogador[Linha - 1][Coluna - 1] == "S":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                submarino[0] -= 1
                return True
            elif tabuleiro2jogador[Linha - 1][Coluna - 1] == "D":
                computador2feedback[Linha - 1][Coluna - 1] = "X"
                destroier[0] -= 1
                return True
            else:
                 computador2feedback[Linha - 1][Coluna - 1] = "N"
                 return False

#verificando a vitoria
def verificacao():
    if quantidade_embarcaçoes[0] == 0:
        print()
        print("O Computador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique & Davi")
        return True

    if quantidade_embarcaçoes[1] == 0:
        print()
        print("O Jogador venceu! \n Muito obrigado por jogar! \n Programa feito por Kaique & Davi")
        return True
    else:
        return False

# Rodada
def rodada(modo):
    if modo == 1:
        print("--------------------------------")
        print("      TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(tabuleiro)):
            print(tabuleiro[linha])    
        print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])
        print("--------------------------------")
        print("         SEU TABULEIRO")
        print("--------------------------------")
        for linha in range(len(computadorfeedback)):
            print(computadorfeedback[linha])
        print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
            
        #Rodada do jogador
        if ataque_jogador(modo) == True:
            print("Fogo! Você acertou! ")
            quantidade_embarcaçoes[1] -= 1
            print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])
            if verificacao() == True:
                return

        else:
            print("Água! Você errou.")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!")
            quantidade_embarcaçoes[0] -= 1
            print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
            
        else:
            print("Água! O computador errou.")
        if verificacao() == False:
            rodada(modo)
             

    elif modo == 2:
        print("--------------------------------")
        print("       TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(tabuleiro2)):
            print(tabuleiro2[linha])  
        print("barcos do computador restantes: ", quantidade_embarcaçoes[1])
        print("--------------------------------")
        print("          SEU TABULEIRO")
        print("--------------------------------")
        for linha in range(len(computador2feedback)):
            print(computador2feedback[linha])
        print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])

        #Rodada do jogador
        if ataque_jogador(modo) == True:
            print("Fogo! Você acertou!")
            quantidade_embarcaçoes[1] -= 1
            print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])
            if verificacao() == True:
                return
            
        else:
            print("Água! Você errou.")

        #Rodada do computador
        if ataque_computador(modo) == True:
            print("Fogo! O computador acertou!")
            quantidade_embarcaçoes[0] -= 1
            print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
                
        else:
            print("Água! O computador errou.")
        if verificacao() == False:
            rodada(modo)
    
    elif modo == 3:
        print("--------------------------------")
        print("       TABULEIRO ADVERSÁRIO")
        print("--------------------------------")
        for linha in range(len(tabuleiro2)):
            print(tabuleiro2[linha])  
        print("barcos do computador restantes: ", quantidade_embarcaçoes[1])
        print("--------------------------------")
        print("          SEU TABULEIRO")
        print("--------------------------------")
        for linha in range(len(computador2feedback)):
            print(computador2feedback[linha])
        print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])

         #Rodada do jogador
        joga_novamente = True
        while joga_novamente:
            joga_novamente = False
            if ataque_jogador(modo) == True:
                print("Fogo! Você acertou!")
                if porta_avioes[1] == 0:
                    print("\nPorta aviões destruído! Jogue novamente.")
                    quantidade_embarcaçoes[1] -= 1
                    joga_novamente = True
                elif navio_tanque[1] == 0:
                    print("\nNavío-Tanque destruído!")
                    quantidade_embarcaçoes[1] -= 1
                    joga_novamente = True
                elif contratorpedeiro[1] == 0:
                    print("\nContratorpedeiro destruído! Jogue novamente")
                    quantidade_embarcaçoes[1] -= 1
                    joga_novamente = True
                elif submarino[1] == 0:
                    print("\Submarino destruído! Jogue novamente")
                    quantidade_embarcaçoes[1] -= 1
                    joga_novamente = True
                elif destroier[1] == 0:
                    print("\Destroier destruído! Jogue novamente")
                    quantidade_embarcaçoes[1] -= 1
                    joga_novamente = True
                print("Barcos do computador restantes: ", quantidade_embarcaçoes[1])
            else:
                print("Água! Você errou.")
                joga_novamente = False

            if verificacao() == True:
                return
        #Rodada do computador
        joga_novamente = True
        while joga_novamente:
            joga_novamente = False
            if ataque_computador(modo) == True:
                print("Fogo! O Computador acertou!")
                if porta_avioes[0] == 0:
                    print("\nPorta aviões destruído! Computador novamente.")
                    quantidade_embarcaçoes[0] -= 1
                    joga_novamente = True
                elif navio_tanque[0] == 0:
                    print("\nNavío-Tanque destruído! Computador novamente.")
                    quantidade_embarcaçoes[0] -= 1
                    joga_novamente = True
                elif contratorpedeiro[0] == 0:
                    print("\nContratorpedeiro destruído! Computador novamente.")
                    quantidade_embarcaçoes[0] -= 1
                    joga_novamente = True
                elif submarino[0] == 0:
                    print("\Submarino destruído! Computador novamente.")
                    quantidade_embarcaçoes[0] -= 1
                    joga_novamente = True
                elif destroier[0] == 0:
                    print("\Destroier destruído! COmputador novamente.")
                    quantidade_embarcaçoes[0] -= 1
                    joga_novamente = True
                print("Barcos do jogador restantes: ", quantidade_embarcaçoes[0])
                if verificacao() == True:
                    return(modo)
                
            else:
                print("Água! Você errou.")
                joga_novamente = False
        if verificacao() == False:
            rodada(modo)
#--------------------------------
#     DESAFIO, modo original
#--------------------------------         
def selecao_barcos_jogador(x):
    if x == 0: #Embarcação 5
        print("Porta-aviões, embarcação de 5 posições")
        orientacao = int(input("Escolha a orientaçã\n1 - Horizontal\n2 - Vertical\n"))  #Escolher orientação
        while orientacao != 1 and orientacao != 2:
            orientacao = int(input("Escolha CORRETAMENTE a orientação\n1 - Horizontal\n2 - Vertical\n"))

        if orientacao == 1:
            Linha = int(input("Digite a linha em que você quer colocar: 1-10: "))
            while Linha < 1 or Linha > 10:
                Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-10: "))
            Coluna = int(input("Digite a coluna em que você quer colocar: 1-6: "))
            while Coluna < 1 or Coluna > 6:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-6: "))
            for i in range(5):
                tabuleiro2jogador[Linha - 1][Coluna - 1 + i] = "P"                #Adicionar ao tabuleiro
            for i in range(len(tabuleiro2jogador)):
                print(tabuleiro2jogador[i])
            print()
        if orientacao == 2:
            Linha = int(input("Digite a linha em que você quer colocar: 1-6: "))
            while Linha < 1 or Linha > 6:
                Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-6: "))
            Coluna = int(input("Digite a coluna em que você quer colocar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-10: "))
            for i in range(5):
                tabuleiro2jogador[Linha - 1 + i][Coluna - 1] = "P"
            for i in range(len(tabuleiro2jogador)):
                print(tabuleiro2jogador[i])
            print()
    elif x == 1: #Embarcação 4
        verificador = False
        verificador2 = 0
        while verificador == False:           #Loop para verificar se não está ocupando uma posição preenchida
            print("Navio-tanque, embarcação de 4 posições")
            print("Evite transtornos, verifique onde já está ocupado e NÃO posicione ali\n")
            orientacao = int(input("Escolha a orientaçã\n1 - Horizontal\n2 - Vertical\n"))
            while orientacao != 1 and orientacao != 2:
                orientacao = int(input("Escolha CORRETAMENTE a orientação\n1 - Horizontal\n2 - Vertical\n"))

            if orientacao == 1:
                Linha = int(input("Digite a linha em que você quer colocar: 1-10: "))
                while Linha < 1 or Linha > 10:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-10: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-7: "))
                while Coluna < 1 or Coluna > 7:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-7: "))
                for i in range(4): #Vai verificar todas as posições para ver se não está vazia
                    if tabuleiro2jogador[Linha - 1][Coluna - 1 + i] == 0:
                        verificador2 += 1
                if verificador2 == 4: #Se estiver totalmente livre, verificador2 resulta correto(nesse caso 4) e sai do loop
                    verificador = True    
                else: #Se uma das posições conflitar, o loop retorna para selecionar novamente
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False
                print()
            if orientacao == 2:
                Linha = int(input("Digite a linha em que você quer colocar: 1-7: "))
                while Linha < 1 or Linha > 7:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-7: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-10: "))
                while Coluna < 1 or Coluna > 10:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-10: "))
                for i in range(4):
                    if tabuleiro2jogador[Linha - 1 + i][Coluna - 1] == 0:
                        verificador2 += 1
                if verificador2 == 4:
                    verificador = True    
                else:
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False


        if orientacao == 1: #Após ver que está 100% livre, ele sai do loop e então preenche as posições
            for i in range(4):
                tabuleiro2jogador[Linha - 1][Coluna - 1 + i] = "T"
        elif orientacao == 2:
            for i in range(4):
                tabuleiro2jogador[Linha - 1 + i][Coluna - 1] = "T"
        for i in range(len(tabuleiro2jogador)): #Para ver como está o tabuleiro
            print(tabuleiro2jogador[i])
        print()


    elif x == 2: #Embarcação 3
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador
            print("Contratorpedeiro, embarcação de 3 posições")
            print("Evite transtornos, verifique onde já está ocupado e NÃO posicione ali\n")
            orientacao = int(input("Escolha a orientaçã\n1 - Horizontal\n2 - Vertical\n")) 
            while orientacao != 1 and orientacao != 2:
                orientacao = int(input("Escolha CORRETAMENTE a orientação\n1 - Horizontal\n2 - Vertical\n"))
            
            if orientacao == 1:
                Linha = int(input("Digite a linha em que você quer colocar: 1-10: "))
                while Linha < 1 or Linha > 10:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-10: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-8: "))
                while Coluna < 1 or Coluna > 8:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-8: "))
                for i in range(3): 
                    if tabuleiro2jogador[Linha - 1][Coluna - 1 + i] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 3: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False
                print()
            if orientacao == 2:
                Linha = int(input("Digite a linha em que você quer colocar: 1-8: "))
                while Linha < 1 or Linha > 8:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-8: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-10: "))
                while Coluna < 1 or Coluna > 10:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-10: "))
                for i in range(3):
                    if tabuleiro2jogador[Linha - 1 + i][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 3: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False

        if orientacao == 1: #Preencher o tabuleiro conforme orientação
            for i in range(3):
                tabuleiro2jogador[Linha - 1][Coluna - 1 + i] = "C"
        elif orientacao == 2: #Preencher o tabuleiro conforme orientação
            for i in range(3):
                tabuleiro2jogador[Linha - 1 + i][Coluna - 1] = "C"
        for i in range(len(tabuleiro2jogador)): #Printar atual tabuleiro
            print(tabuleiro2jogador[i])

    elif x == 3: #Embarcação 2
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador
            print("Submarino, embarcação de 2 posições")
            print("Evite transtornos, verifique onde já está ocupado e NÃO posicione ali\n")
            orientacao = int(input("Escolha a orientaçã\n1 - Horizontal\n2 - Vertical\n"))
            while orientacao != 1 and orientacao != 2:
                orientacao = int(input("Escolha CORRETAMENTE a orientação\n1 - Horizontal\n2 - Vertical\n"))
            
            if orientacao == 1:
                Linha = int(input("Digite a linha em que você quer colocar: 1-10: "))
                while Linha < 1 or Linha > 10:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-10: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-9: "))
                while Coluna < 1 or Coluna > 9:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-9: "))
                for i in range(2): 
                    if tabuleiro2jogador[Linha - 1][Coluna - 1 + i] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 2: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else:
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False
                print()
            if orientacao == 2:
                Linha = int(input("Digite a linha em que você quer colocar: 1-9: "))
                while Linha < 1 or Linha > 9:
                    Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-9: "))
                Coluna = int(input("Digite a coluna em que você quer colocar: 1-10: "))
                while Coluna < 1 or Coluna > 10:
                    Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-10: "))
                for i in range(2): 
                    if tabuleiro2jogador[Linha - 1 + i][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 2: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                    verificador = False
        if orientacao == 1: #Preencher o tabuleiro conforme orientação
            for i in range(2):
                tabuleiro2jogador[Linha - 1][Coluna - 1 + i] = "S"
        elif orientacao == 2: #Preencher o tabuleiro conforme orientação
            for i in range(2):
                tabuleiro2jogador[Linha - 1 + i][Coluna - 1] = "S"
        for i in range(len(tabuleiro2jogador)): #Printar atual tabuleiro
            print(tabuleiro2jogador[i])
    elif x == 4: #Embarcação 1
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador
            print("Destroier, embarcação de 1 posição")
            print("Evite transtornos, verifique onde já está ocupado e NÃO posicione ali\n")
            
            Linha = int(input("Digite a linha em que você quer colocar: 1-10: "))
            while Linha < 1 or Linha > 10:
                Linha = int(input("Digite CORRETAMENTE linha em que você quer colocar: 1-10: "))
            Coluna = int(input("Digite a coluna em que você quer colocar: 1-10: "))
            while Coluna < 1 or Coluna > 10:
                Coluna = int(input("Digite CORRETAMENTE a coluna em que você quer colocar: 1-10: "))

            if tabuleiro2jogador[Linha - 1][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
            if verificador2 == 1: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
            else:  #Algum preenchido, refazer escolhas
                print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
                verificador = False
            print()

        tabuleiro2jogador[Linha - 1][Coluna - 1] = "D" #Preencher o tabuleiro
        for i in range(len(tabuleiro2jogador)):
            print(tabuleiro2jogador[i]) #Printar atual tabuleiro

def selecao_barcos_pc(x):
    if x == 0: #Embarcação 5
        orientacao = random.randint(1,2)  #Escolher orientação
        if orientacao == 1:
            Linha = random.randint(1,10)
            Coluna = random.randint(1-6)
            for i in range(5):
                tabuleiro2computador[Linha - 1][Coluna - 1 + i] = "P"                #Adicionar ao tabuleiro
        if orientacao == 2:
            Linha = random.randint(1,6)
            Coluna = random.randint(1,10)
            for i in range(5):
                tabuleiro2computador[Linha - 1 + i][Coluna - 1] = "P"

    elif x == 1: #Embarcação 4
        verificador = False
        verificador2 = 0
        while verificador == False:           #Loop para verificar se não está ocupando uma posição preenchida

            orientacao = random.randint(1,2)
            if orientacao == 1:
                Linha = random.randint(1,10)
                Coluna = random.randint(1,7)
                for i in range(4): #Vai verificar todas as posições para ver se não está vazia
                    if tabuleiro2computador[Linha - 1][Coluna - 1 + i] == 0:
                        verificador2 += 1
                if verificador2 == 4: #Se estiver totalmente livre, verificador2 resulta correto(nesse caso 4) e sai do loop
                    verificador = True    
                else: #Se uma das posições conflitar, o loop retorna para selecionar novamente
                    verificador = False
                
            if orientacao == 2:
                Linha = random.randint(1,7)
                Coluna = random.randint(1,10)
                for i in range(4):
                    if tabuleiro2computador[Linha - 1 + i][Coluna - 1] == 0:
                        verificador2 += 1
                if verificador2 == 4:
                    verificador = True    
                else:
                    verificador = False


        if orientacao == 1: #Após ver que está 100% livre, ele sai do loop e então preenche as posições
            for i in range(4):
                tabuleiro2computador[Linha - 1][Coluna - 1 + i] = "T"
        elif orientacao == 2:
            for i in range(4):
                tabuleiro2computador[Linha - 1 + i][Coluna - 1] = "T"

    elif x == 2: #Embarcação 3
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador

            orientacao = random.randint(1,2) 
            
            if orientacao == 1:
                Linha = random.randint(1,10)
                Coluna = random.randint(1,8)
                for i in range(3): 
                    if tabuleiro2computador[Linha - 1][Coluna - 1 + i] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 3: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    verificador = False
            if orientacao == 2:
                Linha = random.randint(1,8)
                Coluna = random.randint(1,10)
                for i in range(3):
                    if tabuleiro2computador[Linha - 1 + i][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 3: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    verificador = False

        if orientacao == 1: #Preencher o tabuleiro conforme orientação
            for i in range(3):
                tabuleiro2computador[Linha - 1][Coluna - 1 + i] = "C"
        elif orientacao == 2: #Preencher o tabuleiro conforme orientação
            for i in range(3):
                tabuleiro2computador[Linha - 1 + i][Coluna - 1] = "C"

    elif x == 3: #Embarcação 2
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador
            orientacao = random.randint(1,2) 
            
            if orientacao == 1:
                Linha = random.randint(1,10)
                Coluna = random.randint(1,9)
                for i in range(2): 
                    if tabuleiro2computador[Linha - 1][Coluna - 1 + i] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 2: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else:
                    verificador = False
            if orientacao == 2:
                Linha = random.randint(1,9)
                Coluna = random.randint(1,10)
                for i in range(2): 
                    if tabuleiro2computador[Linha - 1 + i][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
                if verificador2 == 2: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
                else: #Algum preenchido, refazer escolhas
                    verificador = False
        if orientacao == 1: #Preencher o tabuleiro conforme orientação
            for i in range(2):
                tabuleiro2computador[Linha - 1][Coluna - 1 + i] = "S"
        elif orientacao == 2: #Preencher o tabuleiro conforme orientação
            for i in range(2):
                tabuleiro2computador[Linha - 1 + i][Coluna - 1] = "S"

    elif x == 4: #Embarcação 1
        verificador = False
        verificador2 = 0
        while verificador == False: #Loop verificador
            
            Linha = random.randint(1,10)
            Coluna = random.randint(1,10)

            if tabuleiro2computador[Linha - 1][Coluna - 1] == 0: #Verificar posições
                        verificador2 += 1
            if verificador2 == 1: #Todos 0(Vazio), soma resulta correto, loop encerra
                    verificador = True    
            else:  #Algum preenchido, refazer escolhas
                verificador = False

        tabuleiro2computador[Linha - 1][Coluna - 1] = "D" #Preencher o tabuleiro

# def verificador_preenchido(w, x, y, z): PROJETO DESCARTADO DE VERIFICAR PREENCHIMENTO NO MODO 3
#     verificador = 0
#     if w == 1:
#         if x == 1:
#             for i in range(4): #Vai verificar todas as posições para ver se não está vazia
#                 if tabuleiro2jogador[y - 1][z - 1 + i] == 0:
#                     verificador += 1    
#             if verificador == 4:
#                 return True
#             else: #Se uma das posições conflitar, o loop retorna para selecionar novamente
#                 print("Não foi possível posicionar sua embarcação pois conflita com a de outra, escolha novamente:")
#                 print()
#                 return False

rodada(selecao(menu()))

