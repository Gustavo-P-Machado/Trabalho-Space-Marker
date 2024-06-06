import pygame, tkinter

#Colocar uma imagem de fundo com algumas estrelinhas uiui
#criar 3 opções: Salvar, Carregar e Excluir as marcações
    #Fazer essas opções funcionarem
#Quando clicar em qualquer lugar da imagem abrir uma caixa de diálogo pedindo par dar um nome a esse ponto
#Mostrar na tela o luagr em que foi clicado, junto das coordenadas da tela
#Criar automaticamente uma linha ligando as estrelas, que mostra as distancia entre cada estrela
#Criar um sistema de salvamento automárico quando o usuário sair do programa
    #Fazer com que a tecla 'esc'  feche o programa, bem como o botão 'x'


pygame.init() #inicia a biblioteca "pygame"
tamanho = (1080, 720) #tamanho da tela
clock = pygame.time.Clock() #define o fps 
tela = pygame.display.set_mode(tamanho) #cria o display da tela
imgicone  = pygame.image.load("assets/icone.png")
icone = pygame.transform.scale(imgicone, (32, 32))
pygame.display.set_icon(icone)
pygame.display.set_caption('Space Marker') #cria o título da tela

picture = pygame.image.load('assets/imgEspaco.jpg')
bg = pygame.transform.scale(picture, (1080, 720))

posX = 0
posY = 0

branco = (255, 255, 255)

def desenhar():
    for num in range(len(estrelas)):
        pygame.draw.circle(tela, branco, estrelas[num], 5, 0)

def linhas():
    #estrelasUltimo = list(estrelas.keys())[-2]
    #pygame.draw.aaline(tela, branco, (posStart), (estrelas[estrelasUltimo]), 2)
    for coord in range(1, len(estrelas)):
        pygame.draw.aaline(tela, branco, estrelas[coord - 1], estrelas[coord], 3)

    
posDict = 0
estrelas = {

}

posStart = 0, 0


while True: #mantém a tela aberta até que a tela seja fechada
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = evento.pos
            posStart = (posX, posY)
            estrelas[posDict] = posX, posY
            posDict += 1
            

    tela.fill(branco)
    tela.blit(bg, (0, 0))
            
    if len(estrelas) >= 2:
        linhas()
        
    desenhar()

    

    pygame.display.update() #diz pra atualizar a tela
    clock.tick(60) #diz que a tela vai ter 60 fps

