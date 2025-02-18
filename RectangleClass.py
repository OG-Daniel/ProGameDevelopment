import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)
pygame.display.update()

#creating rectangle class

class Rect():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#creating instances
green_rect = Rect(green, (50, 20, 100, 100))
red_rect = Rect(red, (150, 200, 150, 150))
blue_rect = Rect(blue, (300, 400, 200, 200))

#accessing methods
green_rect.draw()
blue_rect.draw()
red_rect.draw()

pygame.display.update() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)


#screen.mainloop()
        