import pygame
pygame.init()
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("C:\Aahana\Game Dev 2\lesson 7\sky.png")
#making a sprite class 
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self,keys):
        if keys[pygame.K_UP]:
            self.rect.y-=1
        if keys[pygame.K_DOWN]:
            self.rect.y+=1
        if keys[pygame.K_RIGHT]:
            self.rect.x+=1
        if keys[pygame.K_LEFT]:
            self.rect.x-=1
img=pygame.image.load("C:\Aahana\Game Dev 2\lesson 7\Rocket.png")

rocket=Player(400,300,img)
#making a group for the sprite
round=pygame.sprite.Group()
round.add(rocket)
while True:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    rocket.update(keys) 
    round.draw(screen)
    pygame.display.update()


