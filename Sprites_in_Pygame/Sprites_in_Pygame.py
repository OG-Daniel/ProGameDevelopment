import pygame
pygame.init()
pygame.display.set_caption("rocket in space")
screen_WIDTH = 700
screen_HEIGHT = 500
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

#define the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/OG_Da/Desktop/JetLearn/Pro Game Development/images/character.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

    #Move the sprite based on key pressed
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5 , 0)
        
        #keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_WIDTH:
            self.rect.right = screen_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_HEIGHT:
            self.rect.bottom = screen_HEIGHT

sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)

    #start the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        #get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        #add background image
        screen.blit(pygame.image.load("C:/Users/OG_Da/Desktop/JetLearn/Pro Game Development/images/space.png"), (0, 0))

        #draw the sprites
        sprites.draw(screen)
        pygame.display.update()

startgame()
    












