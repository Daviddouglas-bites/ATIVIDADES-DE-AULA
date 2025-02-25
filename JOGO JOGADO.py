import pygame
import random

# Definindo cores
colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
    "Brown": (165, 42, 42),
    "Pink": (255, 105, 180),
    "Gray": (128, 128, 128),
    "Lime": (0, 255, 0),
    "Teal": (0, 128, 128),
    "Olive": (128, 128, 0),
    "Slate Blue": (106, 90, 205),
    "Gold": (255, 215, 0),
    "Lavender": (230, 230, 250),
    "Peach": (255, 218, 185),
    "Mint": (189, 252, 201),
    "Light Pink": (255, 182, 193),
    "Sky Blue": (135, 206, 235),
    "Light Yellow": (255, 255, 224),
    "Light Green": (144, 238, 144),
    "Dark Gray": (169, 169, 169),
    "Light Gray": (211, 211, 211),
    "Silver": (192, 192, 192),
    "Dim Gray": (105, 105, 105),
}



# Inicializando o Pygame
pygame.init()

# Configurando a tela
LARGURA_TELA = 1000
ALTURA_TELA = 1000
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Labirinto")

# Definindo o tamanho do grid
TAMANHO_CELULA = 40
LINHAS = ALTURA_TELA // TAMANHO_CELULA
COLUNAS = LARGURA_TELA // TAMANHO_CELULA

# Função para criar o labirinto
def gerar_labirinto():
    labirinto = [[1 for _ in range(COLUNAS)] for _ in range(LINHAS)]  # Mapa cheio de muros
    stack = []
    visitados = [[False for _ in range(COLUNAS)] for _ in range(LINHAS)]  # Mapa de visitação
    inicio_x, inicio_y = 1, 1  # Ponto inicial
    labirinto[inicio_y][inicio_x] = 0
    stack.append((inicio_x, inicio_y))
    
    while stack:
        x, y = stack[-1]
        visitados[y][x] = True
        
        # Verifica as células vizinhas
        vizinhos = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < COLUNAS and 0 < ny < LINHAS and not visitados[ny][nx]:
                vizinhos.append((nx, ny))
        
        if vizinhos:
            nx, ny = random.choice(vizinhos)
            labirinto[ny][nx] = 0
            labirinto[(ny + y) // 2][(nx + x) // 2] = 0  # Remove o muro entre as células
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return labirinto

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto):
    for y in range(LINHAS):
        for x in range(COLUNAS):
            cor = PINK if labirinto[y][x] == 0 else BLACK
            pygame.draw.rect(tela, cor, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

# Loop principal do jogo
def main():
    labirinto = gerar_labirinto()
    jogador_x, jogador_y = 1, 1  # Posição inicial do jogador
    clock = pygame.time.Clock()
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
           if labirinto[jogador_y][jogador_x - 1] == 0:
                jogador_x -= 1
        if teclas[pygame.K_RIGHT]  or teclas[pygame.K_d]:
            if labirinto[jogador_y][jogador_x + 1] == 0:
                jogador_x += 1
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            if labirinto[jogador_y - 1][jogador_x] == 0:
                jogador_y -= 1
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
             if labirinto[jogador_y + 1][jogador_x] == 0:
                jogador_y += 1

        
       
      
        # Desenhar o fundo
        tela.fill(WHITE)

        # Desenhar o labirinto
        desenhar_labirinto(labirinto)

        # Desenhar o jogador
        pygame.draw.rect(tela, PINK, (jogador_x * TAMANHO_CELULA, jogador_y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
