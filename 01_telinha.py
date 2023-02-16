import pygame
# Inicializando módulos de Pygame
pygame.init()
# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Olá, mundo!')

deve_continuar = True
# Loop do jogo
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            deve_continuar = False

# Encerrando módulos de Pygame
pygame.quit()
