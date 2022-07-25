#Tests file

'''class Match:
    def __init__(self,hero1,hero2):
        
        self.hero1 = hero1
        self.hero2 = hero2
        self.turnid = 0
        
        self.on_live()
        self.first_play()
        self.shuffledecks()
        self.initdraw()
        self.on_ready()
        
        initdraw = True
        
    def on_live(self):
        print('Partida comecou! %s vs %s.' %(self.hero1.name,self.hero2.name))
        return
    
    def first_play(self):
        r = random.randrange(1,3)
        
        if r == 1:
            self.hero1.turnKey = True
            winner = self.hero1.name
        else:
            self.hero2.turnKey = True
            winner = self.hero2.name
            
        print('%s ganhou na sorte e comeca jogando.' %winner)
        return
    
    def shuffledecks(self):
        self.hero1.deck.shuffle()           #self.hero = objeto da classe hero ...
        self.hero2.deck.shuffle()           #self.hero.deck = lista deck do objeto da classe hero
                                            #self.hero.deck.shuffle() = metodo shuffle da classe deck acessada pelo objeto e agora pela classe Partida.
                                            
    def initdraw(self):
        if self.initdraw is True:
            self.hero1.draw(self.hero1.deck,4)
            self.hero2.draw(self.hero2.deck,4)
            self.initdraw = False   
        else:
            return
        
    def endgame_event(self):
        if self.hero1.life <= 0 or self.hero2.life <= 0:            #se a vida de x ou y zerar, retorna True
            return True
        else:
            return False

    def jogada(self):
        a = 3
        if self.hero1.turnKey is True:
            x = self.hero1
            y = self.hero2
        else:
            x = self.hero2
            y = self.hero1
            
        if self.turnid == 0:
            a = 2
            
        else:
            a += len(x.field)
                   
        while a != 0:
            
            if self.endgame_event():
                return
            
            if a >= 2:
                
                print('[%s] Acoes disponiveis: %i' %(x.name,a))
                jogadai = input('Escolha uma jogada: Invocacao,Magia,Atk,Fusao,Passar turno:\n')
            
                if jogadai == 'Invocacao':
                    if x.summon():      
                        a -= 1
                elif jogadai == 'Magia':
                    print('magia')
                    a -= 1
                elif jogadai == 'Ataque':
                    if x.atk(y):
                        a -= 1
                elif jogadai == 'Fusao':
                    print('fusao')
                    a -= 1
                elif jogadai == 'Passar turno':
                    print('passar turno')
                    self.turnid += 1        #termina o turno
                    return
                else:
                    continue
            
            
            elif a == 1:                        #so resta a acao de pular
                
                print('[%s]Acoes disponiveis: %i' %(x.name,a))
                jogadai = input('[%s]Escolha uma jogada: Passar turno\n' %(x.name))
            
                if jogadai == 'Passar turno' or jogadai == 'passar turno':
                    a = 0
                    self.turnid += 1            #termina o turno
                    return
    
    def turn(self):      
        if self.hero1.turnKey is True:
            'hero1 turno'
            if self.turnid >= 1:
                self.hero1.changeMana(1)
                self.hero1.draw(self.hero1.deck,1)
            self.jogada()
            self.hero1.reset_allatkcard()
            self.hero1.turnKey = False
            self.hero2.turnKey = True
        else:
            'hero2 turno'
            if self.turnid >= 1:
                self.hero2.changeMana(1)
                self.hero2.draw(self.hero2.deck,1)
            self.jogada()
            self.hero2.reset_allatkcard()
            self.hero2.turnKey = False
            self.hero1.turnKey = True
            
    def on_ready(self):
        while True:

            self.turn()
            if self.hero1.life <= 0 and self.hero2.life <= 0:
                print('draw')
                return
            elif self.hero1.life <= 0:
                print('%s ganhou a partida' %self.hero2.name)
                return
            elif self.hero2.life <= 0:
                print('%s ganhou a partida' %self.hero1.name)
                return'''