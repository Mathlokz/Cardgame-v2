import random,pygame,time
from imageNbuttons import *
from pygame.locals import *

pygame.init()
width = 1280
height = 720

game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Yugi fetido')


class Carta:
    def __init__(self,name,cardtype,cardfamily,manacost,effect,info,atk,id,img):
        
        self.name = name                #string
        self.cardtype = cardtype        #string
        self.cardfamily = cardfamily    #string
        self.manacost = manacost        #int
        self.effect = effect            #class
        self.info = info                #string
        self.atk = atk                  #int
        self.id = id                    #int
        self.atkcheck = False           #bool
        self.img = img
        self.getimg()
        
    def __str__(self):
        
        return ('%s-%s-%s [ATK]:%i [ID]:%i' %(self.name,self.cardtype,self.cardfamily,self.atk,self.id))
    
    def reset_attackcheck(self):
        
        self.atkcheck = False
        return
    
    def getimg(self):
        
        self.img = imageMaker('imagens_cardsv2/%s.png' %(self.img),112,158 )
        
Brunao = Carta('Brunao','Monster','Diferenciado',3,'','brunao card info',9,1,'brunao')
Cida = Carta('Cida','Monster','Diferenciado',3,'','cida card info',9,1,'cida')
Matheus = Carta('MTHS','Monster','Diferenciado',3,'','card info',8,1,'matheus')
Renan = Carta('RENAN','Monster','Diferenciado',3,'','card info',7,1,'renan')
Vitinho = Carta('Vitinho','Monster','Diferenciado',3,'','card info',6,1,'vitinho')
Elha = Carta('Elha','Monster','Diferenciado',3,'','card info',5,1,'elha')
Fael = Carta('Fael','Monster','Diferenciado',3,'','card info',4,1,'fael')
Coin = Carta('Coin','Monster','Diferenciado',3,'','card info',3,1,'coin')
Marinho = Carta('Marinho','Monster','Diferenciado',3,'','card info',5,1,'marinho')
Janjao = Carta('Janjao','Monster','Diferenciado',3,'','card info',4,1,'janjao')
Torto = Carta('Torto','Monster','Diferenciado',3,'','card info',5,1,'torto')
Herculao = Carta('Herculao','Monster','Diferenciado',3,'','card info',4,1,'herculao')
Theu = Carta('Theu','Monster','Diferenciado',3,'','card info',3,1,'theu')
Verminho = Carta('Verminho','Monster','Diferenciado',3,'','card info',7,1,'verminho')

monster_cards = {Brunao.name : Brunao, Cida.name : Cida, Matheus.name : Matheus, Renan.name : Renan, Vitinho.name : Vitinho, Elha.name : Elha, Fael.name : Fael, Coin.name : Coin}

###creating images
class Element:
        #main menu
        mainmenu = imageMaker('imagens_menuv2/menu_background.png',width,height)
        menuplay = imageMaker('imagens_menuv2/menu_play.png',303,97)
        menucartas = imageMaker('imagens_menuv2/menu_cards.png',303,97)
        menuoptions = imageMaker('imagens_menuv2/menu_options.png',303,97)
        menuexit = imageMaker('imagens_menuv2/menu_exit.png',303,97)
        #playmenu/online/boss/history
        playmenu = imageMaker('imagens_menuv2/menu_background.png',width,height)
        playonline = imageMaker('imagens_play/online_button.png',303,97)
        playvsboss = imageMaker('imagens_play/vsboss_button.png',303,97)
        playhistory = imageMaker('imagens_play/history_button.png',303,97)
        back = imageMaker('imagens_play/back_button.png',303,97)
    
        arenabackground = imageMaker('imagens_play/multiplayer_background.png',width,height)
        vsboss = imageMaker('imagens_play/vsboss_background.png',width,height)
        TURNBUTTON = imageMaker('imagens_cards/turn_button.png',70,20)
        ATK = imageMaker('imagens_cards/attack_icon.png',30,30)
        SUMON = imageMaker('imagens_cards/summon_icon.png',30,30)

        ###transforming images -> button

        #main menu
        menuplay = Button(menuplay, 483, 93)
        menucartas = Button(menucartas,483, 93 + 152)
        menuoptions = Button(menuoptions,483,93 + 152*2)
        menuexit = Button(menuexit,483, 93 + 152*3)

        #play menu/online/boss/history
        playonline = Button(playonline, 483, 93)
        playvsboss = Button(playvsboss,483, 93 + 152)
        playhistory = Button(playhistory,483,93 + 152*2)
        back = Button(back,483, 93 + 152*3)
        
        TURNBUTTON = Button(TURNBUTTON,1170,350)
        ATK = Button(ATK,200,580)
        SUMON = Button(SUMON,200,620)
        
class Deck:
    def __init__(self):
        
        self.cards = []
        self.build()                #instanciando a funcao build(). Toda vez que um objeto for criado ele roda pelo __init__ a funcao criacao do deck.

    
    def build(self): 
        try:
            while len(self.cards) != 4:     #4 = teste , 20 = padrao
                self.cards.append(monster_cards.popitem())
        except Exception as e:
            print('(Erro) build() nao foi possivel criar o deck:',e)
        else:
            return
        
    def showdeck(self):
        print('Cartas do deck:')
        for n in self.cards:
            print(n)
            
    def shuffle(self):
        for i in range(len(self.cards)-1,0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,life,mana,shield,status,img):
        
        self.name = name
        self.life = life
        self.mana = mana
        self.shield = shield
        self.status = status
        self.img = img
        self.lifeicon = imageMaker('imagens_cards/life_icon.png',50,50)
        self.manaicon = imageMaker('imagens_cards/mana_icon.png',50,50)
        self.shieldicon = imageMaker('imagens_cards/shield_icon.png',50,50)
        
        self.player = None
        self.turnKey = False
        self.deck = Deck()      #todo hero ao ser criado gera seu proprio deck.
        self.getimg()           #retona a self.img uma imagem
        self.hand = []
        self.field = []
        self.graveyard = []
        
    def getimg(self):
        self.img = imageMaker('imagens_heroes/%s.png' %(self.img),90,90)             #retorna a self.img a imagem do hero
    
    def changeLife(self,value):
        if self.life + value > 80:
            self.life = 80
        else:
            self.life += value
        
        if value > 0:
            print('%s ganhou %i pontos de vida. Vida total: %i' %(self.name,value,self.life))
        elif value < 0:
            print('%s perdeu %i pontos de vida. Vida total: %i' %(self.name,value,self.life))
            
    def changeMana(self,value):
        if self.mana + value > 10:
            self.mana = 10
        else:
            self.mana += value
            
        if value > 0:
            print('[%s] ganhou %.2f de mana. Mana total: %.2f' %(self.name,value,self.mana))
        elif value < 0:
            print('[%s] perdeu %.2f de mana. Mana total: %.2f' %(self.name,value,self.mana))
        
    def changeShield(self,value):
        self.shield += value
        
        if value > 0:
            print('[%s] ganhou %i de shield. Shield total: %i' %(self.name,value,self.shield))
        elif value < 0:
            print('[%s] perdeu %i de shield. Shield total: %i' %(self.name,value,self.shield))

    def draw(self,deck,amount):
        try:
            for i in range(amount):
                if len(self.hand) < 6:
                    self.hand.append(deck.drawCard())
                elif len(self.hand) >= 6:
                    print('[%s]Mao cheia, carta queimada.' %self.name)
                    null = self.deck.drawCard()
                    null = 0
        except Exception as e:
            print('Sem cartas no baralho, draw() falhou:', e)
            self.changeLife(-10)
            return False
        else:
            return True
        
    def sendtogy(self,target):
        try:
            for card in self.field:
                if target == card[1]:
                    
                    self.graveyard.append(card)
                    self.field.remove(card)
                    
                    print('%s foi mandado para o cemiterio' %(card[0]))
        except Exception as e:
            print('Algum erro ocorreu, sendtogy() falhou:', e)
        else:
            return
    
    def showHand(self):
        print('Cartas na mao: %i' %(len(self.hand)))
        
        for card in self.hand:
            print(card[1])          #retorna o objeto ..... card[0] = card.name card[1] = object card
        return  
    
    def showField(self):
        print('Cartas no campo: %i' %(len(self.field)))
        
        for card in self.field:
            print(card[1])
            
        return          
            
    def showGy(self):
        print('Cartas no cemiterio: %i' %(len(self.graveyard)))

        for card in self.graveyard:
            print(card[1])

        return          
    
    def summon(self):  
        print('Summon triggered')
        
        print('Sua mao:')
        self.showHand()
        
        while True:
            
            sum = str(input('Faca um summon ((abort) se quiser cancelar):\n'))
            
            if sum == 'abort':
                print('Summon cancelado.')
                return False
        
            for card in self.hand:
                
                if sum == card[0]:
                    manacost = card[1].manacost
                    
                    if self.mana >= manacost:
                        'have mana'
                        self.field.append(card)
                        self.hand.remove(card)
                        print('%s sumonou %s' %(self.name,card[0]))
                        self.changeMana(-manacost)
                        return True
                    else:
                        'no have mana'
                
            print('Summon invalido, tente novamente.')

    def summonrandom(self):
        try:
            r = random.randrange(len(self.hand))
            
            getcard = self.hand.pop(r)
            
            self.field.append(getcard)
            
            mana = getcard[1].manacost
            print('[%s] sumonou %s aleatoriamente.' %(self.name,getcard[0]))
            self.changeMana(-mana)
        except Exception as e:
            print('(Error) in summonrandom():', e)
        else:
            return
    
    def atk(self,target):
        bol = False
        h = False
        if len(self.field) > 0 :
            
            while True:
                self.showField()
                atkmonster = input('Escolha um monstro para usar (use (abort) para cancelar):\n')
                
                if atkmonster == 'abort' or atkmonster == 'Abort':
                    return False
                    
                for monster in self.field:
                    if atkmonster == monster[0] and monster[1].atkcheck is True:
                        print('[%s] Monstro ja atacou' %monster[1].name)
                        bol = False
                        
                    elif atkmonster == monster[0] and monster[1].atkcheck is False:
                        atkmonster = monster[1]    
                        bol = True
                        break
                
                if bol is True:
                    break    
                
                print('Alvo invalido (%s)' %atkmonster)      
            
            if len(target.field) > 0:
                
                while True:
                    
                    target.showField()
                    targetmonster = input('Escolha um alvo (use(abort) para cancelar):\n')
                    
                    if targetmonster == 'abort' or atkmonster == 'Abort':
                        return False
                    
                    for monsterX in target.field:
                        if targetmonster == monsterX[0]:
                            targetmonster = monsterX[1]
                            h = True
                            break
            
                    if h is True:
                        break
                    
                    print('Alvo invalido (%s)' %targetmonster)
                
                if atkmonster.atk > targetmonster.atk:
                    'win trade'
                    
                    target.sendtogy(targetmonster)
                    dmg = atkmonster.atk - targetmonster.atk
                    target.changeLife(-dmg)
                    atkmonster.atkcheck = True
                    return True
                    
                elif atkmonster.atk < targetmonster.atk:
                    'lose trade'
                    
                    self.sendtogy(atkmonster)
                    dmg = targetmonster.atk - atkmonster.atk
                    self.changeLife(-dmg)
                    atkmonster.atkcheck = True
                    return True
                else:
                    'both die'
                    
                    self.sendtogy(atkmonster)
                    target.sendtogy(targetmonster)
                    return True

            elif len(target.field) <= 0:
                #add select hero
                dmg = atkmonster.atk
                target.changeLife(-dmg)
                atkmonster.atkcheck = True
                return True
        
        else:
            print('Voce nao tem cartas no campo')
            return False
    
    def reset_allatkcard(self):
        for card in self.field:
            card[1].reset_attackcheck()

    def spellscard(self):
        ''
        
class Vsboss():
    
    def __init__(self,player):
        
        self.player = player
        self.turnid = 0
        
        self.shuffledecks()
        self.initdraw()
        #self.on_ready_showHandcards()
    
        initdraw = True    
        
    def shuffledecks(self):
        self.player.deck.shuffle()
                                            
    def initdraw(self):
        if self.initdraw is True:
            self.player.draw(self.player.deck,4)
            self.initdraw = False
            print(self.player.hand)
            return True 
        else:
            return False
        
        
    def endgame_event(self):
        if self.player.life <= 0:
            return True
        else:
            return False
        
    playerhand_buttons = []
        
    '''def on_ready_showHandcards(self):
        x = 350
        y = 558
        for carta in self.player.hand:
            imageShow(game_screen,self.player.img,x,y)
            x += 117'''