import pygame
from tkinter import simpledialog, messagebox



# Inicaliza o Pygame
pygame.init() 

# Configura a janela do Pygame
tamanho = 1080, 720
tela = pygame.display.set_mode(tamanho, pygame.RESIZABLE) 
imgicone  = pygame.image.load("assets/icone.png")
icone = pygame.transform.scale(imgicone, (32, 32))
picture = pygame.image.load('assets/imagemFundo.png')
bg = pygame.transform.scale(picture, tamanho)

# Configura o icone e título do Pygame
pygame.display.set_icon(icone)
pygame.display.set_caption('Space Marker')
fonte = pygame.font.SysFont('comicsans', 25)
fonteOpcoes = pygame.font.SysFont('times', 20)


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
marcacoes = {}
estrelas = {}
vazio = str('')
tela.fill(branco)
tela.blit(bg, (0, 0))

posX = 0
posY = 0


# Loop principal do jogo
jogando = True
while jogando:


    for event in pygame.event.get():

        if event.type == pygame.WINDOWRESIZED:
            tamanho = tela.get_width(), tela.get_height()
            bg = pygame.transform.scale(picture, tamanho)
            tela.fill(branco)
            tela.blit(bg, (0, 0))

        if event.type == pygame.QUIT:
            arquivoExt = arquivo = open("salvamento.trab", "w", encoding="utf-8")
            arquivo.write(str(estrelas) + '\n')
            arquivo.write(str(marcacoes) + '\n')
            arquivo.write(str(posDict))
            arquivo.close()

            jogando = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            arquivoExt = arquivo = open("salvamento.trab", "w", encoding="utf-8")
            arquivo.write(str(estrelas) + '\n')
            arquivo.write(str(marcacoes) + '\n')
            arquivo.write(str(posDict))
            arquivo.close()

            jogando = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            posX, posY = event.pos
            posStart = (posX, posY)

            posicaoEstrela = pygame.mouse.get_pos()

            nomeEstrela = simpledialog.askstring("Space Marker", "Nome Da Estrela:")
            
            

            if nomeEstrela != None:
                
                estrelas[posDict] = posX, posY
                posDict += 1
                marcacoes[posicaoEstrela] = nomeEstrela


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            
            arquivoExt = arquivo = open("salvamento.trab", "w", encoding="utf-8")
            arquivo.write(str(estrelas) + '\n')
            arquivo.write(str(marcacoes) + '\n')
            arquivo.write(str(posDict))
            arquivo.close()
            messagebox.showinfo('Salvamento', 'Marcações salvas com sucesso')

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                arquivo = open("salvamento.trab", "r", encoding="utf-8")
                linhasExt = arquivo.readlines()
                estrelas = eval(linhasExt[0])
                marcacoes = eval(linhasExt[1])
                posDict = eval(linhasExt[2])
            except:
                messagebox.showerror('ERRO DE CARREGAMENTO', 'ARQUIVO DE SALVAMENTO NÃO ENCONTRADO')

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            arquivoExt = arquivo = open("salvamento.trab", "w", encoding="utf-8")
            arquivo.write(str(vazio) + '\n')
            arquivo.close
            marcacoes = {}
            estrelas = {}
            posX = 0
            posY = 0
            posDict = 0
            posStart = 0, 0
            tela.fill(branco)
            tela.blit(bg, (0, 0))


    for posicao, nomeEstrela in marcacoes.items():

        if not nomeEstrela.strip() == '':
            texto = fonte.render(nomeEstrela, True, branco)
            tela.blit(texto, posicao )
        else:
            texto = fonte.render('Desconhecido' + str(posicao), True, branco)        
            tela.blit(texto, posicao)
            

    textoOpcoesF10 = fonteOpcoes.render('F10 para salvar as marcações', True, branco)
    textoOpcoesF11 = fonteOpcoes.render('F11 para carregar as marcações', True, branco)
    textoOpcoesF12 = fonteOpcoes.render('F12 para excluir as marcações', True, branco)

    tela.blit(textoOpcoesF10, (0, 0))
    tela.blit(textoOpcoesF11, (0, 25))
    tela.blit(textoOpcoesF12, (0, 50))
    desenhar()
    linhas()
        


    # Atualiza a tela    
    pygame.display.update() 

# Finaliza o Pygame
pygame.quit()

    


    

    

    

    




