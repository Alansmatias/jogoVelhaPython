def exibir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print("|".join(map(str, linha)))
        if i < 2:
            print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    jogador_atual = 'X'

    for _ in range(9):  # Máximo de 9 jogadas em um jogo da velha
        exibir_tabuleiro(tabuleiro)
        escolha = int(input(f"Jogador {jogador_atual}, escolha um número de 1 a 9: "))

        # Mapear a escolha do jogador para as coordenadas da matriz
        linha = (escolha - 1) // 3
        coluna = (escolha - 1) % 3

        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns, Jogador {jogador_atual}! Você venceu!")
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Essa posição já está ocupada. Escolha outra.")

    else:
        exibir_tabuleiro(tabuleiro)
        print("O jogo terminou em empate.")

# Iniciar o jogo
jogar_jogo_da_velha()
