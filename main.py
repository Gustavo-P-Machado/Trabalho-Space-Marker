import pygame

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
pygame.display.set_caption('Space Marker') #cria o título da tela

picture = pygame.image.load('recursos/imgEspaco.jpg')
bg = pygame.transform.scale(picture, (1080, 720))

branco = (255, 255, 255)
while True: #mantém a tela aberta até que a tela seja fechada
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    
    tela.fill(branco)
    tela.blit(bg, (0, 0))


    pygame.display.update() #diz pra atualizar a tela
    clock.tick(60) #diz que a tela vai ter 60 fps

pygame.quit()