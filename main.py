from classes import *       # import of scripts -

#Creating heroes
Slark = Player('Slark',80,5,5,0,'slark')
Pudge = Player('Pudge',80,5,5,0,'pudge')

class gameNAV:      # Game Navigation 
    loadgame = True
    inMenu = True
    inPlay = False
    inOnline = False
    inVsboss = False
    inHistory = False
    inCards = False
    inOptions = False
    
    def MAINMENU():
        if gameNAV.inMenu is True:            #mostra o menu inicial se inMenu == True

            imageShow(game_screen,Element.mainmenu,0,0)

            if Element.menuplay.draw(game_screen):
                gameNAV.inMenu = False
                gameNAV.inPlay = True
                time.sleep(0.15)
                
            if Element.menucartas.draw(game_screen):
                #gameNAV.inMenu = False
                #gameNAV.inCards = True
                print('menu cards')
                time.sleep(0.15)
                
            if Element.menuoptions.draw(game_screen):
                #gameNAV.inMenu = False
                #gameNAV.inOptions = True
                print('options')
                time.sleep(0.15)

            if Element.menuexit.draw(game_screen):
                print('exit')
                gameNAV.loadgame = False
                time.sleep(0.15)
        
    def PLAYMENU():
        if gameNAV.inPlay is True:      #mostra o menu play -- partida
            
            imageShow(game_screen,Element.playmenu,0,0)
            
            if Element.playonline.draw(game_screen):
                #gameNAV.inPlay = False
                #gameNAV.inOnline = True
                print('play online')
                time.sleep(0.15)
                
            if Element.playvsboss.draw(game_screen):
                gameNAV.inPlay = False
                gameNAV.inVsboss = True
                print('play vs boss')
                time.sleep(0.15)
                
            if Element.playhistory.draw(game_screen):
                #gameNAV.inPlay = False
                #gameNAV.inHistory = True
                print('play history')
                time.sleep(0.15)

            if Element.back.draw(game_screen):
                gameNAV.inPlay = False
                gameNAV.inMenu = True
                print('voltar')
                time.sleep(0.15)    
        
    def ONLINE():
        if gameNAV.inOnline is True:     #mostra o menu de cartas
            pass

    def VSBOSS():
        if gameNAV.inVsboss is True:     #mostra o menu de cartas
            imageShow(game_screen,Element.vsboss,0,0)
            Vsboss(Slark)

        
             
    def HISTORY():
        if gameNAV.inHistory is True:     #mostra o menu de cartas
            pass
    
    def CARDS():
        if gameNAV.inCards is True:     #mostra o menu de cartas
            pass
    
    def OPTIONS():
        if gameNAV.inOptions is True:     #mostra o menu de cartas
            pass
        

while gameNAV.loadgame:                        #LOOP DO JOGO

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameNAV.loadgame = False
                
    gameNAV.MAINMENU()
    gameNAV.PLAYMENU()
    gameNAV.ONLINE()
    gameNAV.VSBOSS()
    gameNAV.HISTORY()
    gameNAV.CARDS()
    gameNAV.OPTIONS()
        
    pygame.display.update()