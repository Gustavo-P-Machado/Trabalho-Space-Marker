import pygame
from tkinter import simpledialog


# Inicaliza o Pygame
pygame.init() 

# Configura a janela do Pygame
tamanho = (1080, 720)
tela = pygame.display.set_mode(tamanho) 
imgicone  = pygame.image.load("assets/icone.png")
icone = pygame.transform.scale(imgicone, (32, 32))
picture = pygame.image.load('assets/imgEspaco.jpg')
bg = pygame.transform.scale(picture, (1080, 720))

# Configura o icone e título do Pygame
pygame.display.set_icon(icone)
pygame.display.set_caption('Space Marker')

# Funções
def linhas():
    for coord in range(1, len(estrelas)):
        pygame.draw.aaline(tela, branco, estrelas[coord - 1], estrelas[coord], 3)

def desenhar():
    for num in range(len(estrelas)):
        pygame.draw.circle(tela, branco, estrelas[num], 5, 0)

# Variáveis Loop
posDict = 0
posStart = 0, 0
branco = (255,255,255)
estrelas = {}
tela.fill(branco)
tela.blit(bg, (0, 0))

posX = 0
posY = 0

# Loop principal do jogo
jogando = True
while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = event.pos
            posStart = (posX, posY)
            estrelas[posDict] = posX, posY
            posDict += 1
        

    #if len(estrelas) >= 2:
    linhas()
        
    desenhar()


    # Atualiza a tela    
    pygame.display.update() 

# Finaliza o Pygame
pygame.quit()

    


    

    

    

    




