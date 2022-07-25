import pygame
width = 1280
height = 720

def imageMaker(image, width, height):
    card = pygame.image.load(image).convert_alpha()
    card = pygame.transform.scale(card, (width, height))
    return card

def imageShow(screens,image,x,y):
    card = screens.blit(image,(x,y))
    return card

class Button:
    def __init__(self,image,x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self,surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        #pode clicar mais de 1x
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action