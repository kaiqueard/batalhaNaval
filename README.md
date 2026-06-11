# Batalha Naval 🚢

Trabalho Avaliativo Somatório sobre Batalha Naval - Ciência da Computação; 
Feito no 1° Período.

# Funcionalidades

O jogo funciona no modo Jogador x Computador;

Tem três modos de jogo:
- Tabuleiro 5x10;
- Tabuleiro 10x10;
- Desafio 10x10.

# Tabuleiros

Cada jogador tem 2 tabuleiros (por modo):
- Um tabuleiro onde ficam guardadas as posições dos barcos;
- Um de feedback (onde os jogadores irão atacar) para a rodada principal.

# Desafio

Tabuleiro 10x10 com 5 embarcações de tamanhos diferentes (1 a 5 posições);

Embarcação só afunda quando todas as suas posições forem atingidas;

Ao afundar uma embarcação, o jogador ataca novamente;

Vence quem afundar toda a frota inimiga primeiro.

# Regras

Para cada modo de jogo Usuário e Computador devem escolher 5 posições para colocarem seus barcos;

Após escolherem as posições, o verdadeiro jogo começa. Usuário e Computador escolhem uma posição para atacarem no tabuleiro inimigo;

O jogo só encerra quando TODAS as embarcações inimigas forem afundadas.

## Demonstração
| Tabuleio 5x10 | Tabuleiro 10x10 | Desafio |
|----------|--------------|-----------|
| ![](.//gifs/5x10.gif) | ![](.//gifs/10x10.gif) | ![](.//gifs/desafio.gif) |
  
# Linguagem

Feito exclusivamente em python.

# Como rodar

bash (Abra o git bash);

git clone https://github.com/kaiqueard/batalhaNaval (Clone a pasta do GitHub para sua máquina);

cd batalhaNaval (Abra ela);

python main.py (Inicie em Python).

# Curiosidade

O código está modulado em funções.

# Autores

Kaique Buchoski & Davi Sequinel.
