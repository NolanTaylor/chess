import pygame
import sys
import os

pygame.init()

_image_library = {}
v = 1
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = pygame.transform.rotozoom(image, 0, v)
                _image_library[path] = image
        return image

def blit(png, x, y):
    screen.blit(get_image(png), ((SWidth/2) - v * (img.get_width()/x), (SHeight/2) - v * (img.get_height()/y)))

screen = pygame.display.set_mode((900, 750), pygame.RESIZABLE)
img = pygame.image.load('ImageCalibrator1.png').convert()
pressed = pygame.key.get_pressed()
done = False
Quit = False

while not done:
    #Mouse Coordinates
    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    #Size of Window
    SWidth, SHeight = pygame.display.get_surface().get_size()

    screen.fill((255, 255, 255))

    blit('Board.png', 2, 2)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.QUIT or Quit == True:
            done = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            ReSizeHold = False
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)