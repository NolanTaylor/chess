import pygame
import sys
import os

pygame.init()

_image_library = {} #images already used
v = 1 #scale
def get_image(path): #loads an image from given path
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = pygame.transform.rotozoom(image, 0, v)
                _image_library[path] = image
        return image

def blit(png, x, y, addposx, addposy, addmovx, addmovy): #blits an image (duh)
    if addposx != None and addposy != None:
        screen.blit(get_image(png), ((SWidth/2) - v * (img.get_width()/x) + addposx * img.get_width()/10.5 + addmovx, (SHeight/2) - v * (img.get_height()/y) + addposy * img.get_height()/8 + addmovy))
    else:
        pass

def draw(x, y, w, h): #only used for finding square positions prolly not necessary anymoar
    pygame.draw.rect(screen, (255, 155, 155), [(SWidth/2) - v * (img.get_width()/x), (SHeight/2) - v * (img.get_height()/y), img.get_width()/w, img.get_height()/h])

def square(x, y): #find what square the mouse is on
    pos = [0, 0]

    if x >= (SWidth/2) - v * (img.get_width()/2.66) and x <= (SWidth/2) - v * (img.get_width()/2.66) + img.get_width()/10.5:
        pos[0] = 0
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 2 * img.get_width()/10.5:
        pos[0] = 1
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 2 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 3 * img.get_width()/10.5:
        pos[0] = 2
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 3 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 4 * img.get_width()/10.5:
        pos[0] = 3
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 4 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 5 * img.get_width()/10.5:
        pos[0] = 4
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 5 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 6 * img.get_width()/10.5:
        pos[0] = 5
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 6 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 7 * img.get_width()/10.5:
        pos[0] = 6
    elif x >= (SWidth/2) - v * (img.get_width()/2.66) + 7 * img.get_width()/10.5 and x <= (SWidth/2) - v * (img.get_width()/2.66) + 8 * img.get_width()/10.5:
        pos[0] = 7
    else:
        pos[0] = None

    if y >= (SHeight/2) - v * (img.get_height()/2) and y <= (SHeight/2) - v * (img.get_height()/2) + img.get_height()/8:
        pos[1] = 0
    elif y >= (SHeight/2) - v * (img.get_height()/2) + img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 2 * img.get_height()/8:
        pos[1] = 1
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 2 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 3 * img.get_height()/8:
        pos[1] = 2
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 3 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 4 * img.get_height()/8:
        pos[1] = 3
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 4 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 5 * img.get_height()/8:
        pos[1] = 4
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 5 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 6 * img.get_height()/8:
        pos[1] = 5
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 6 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 7 * img.get_height()/8:
        pos[1] = 6
    elif y >= (SHeight/2) - v * (img.get_height()/2) + 7 * img.get_height()/8 and y <= (SHeight/2) - v * (img.get_height()/2) + 8 * img.get_height()/8:
        pos[1] = 7
    else:
        pos[1] = None

    #frickin' python doesn't have switch statements

    return pos

class Actor: #basically chess piece
    def __init__(self, position, moved, lifted, piece):
        self.pos = position #position of piece on board
        self.mov = moved #position of piece when being lifted and moved
        self.lif = lifted #piece is lifted or not
        self.piece = piece #type of piece

    def move(self): #for moving the piece
        if square(Mouse_x, Mouse_y) == [self.pos[0], self.pos[1]] and click: #if mouse is on same square as piece and mouse is clicked
            global addStatic
            addStatic = [Mouse_x, Mouse_y] #anchor for adding value to piece position
            self.lif = True #piece is lifted

        if self.lif and not click: #piece is put down
            self.pos[0] = square(Mouse_x, Mouse_y)[0]
            self.pos[1] = square(Mouse_x, Mouse_y)[1] #center piece on square
            self.lif = False #piece is not lifted anymoar

class Rook(Actor): #Rook (duh)
    def show(self): #blits image
        if self.lif:
            add[0] = Mouse_x - addStatic[0]
            add[1] = Mouse_y - addStatic[1]
            blit('C:\PythonPrograms\Chess\{0}.png'.format(self.piece), 1.2, 1.065, self.pos[0], self.pos[1], add[0], add[1])
        else:
            blit('C:\PythonPrograms\Chess\{0}.png'.format(self.piece), 1.2, 1.065, self.pos[0], self.pos[1], 0, 0)

screen = pygame.display.set_mode((900, 750), pygame.RESIZABLE)
img = pygame.image.load('C:\PythonPrograms\Chess\ImageCalibrator1.png').convert()
pressed = pygame.key.get_pressed()
done = False
Quit = False
add = [0, 0]
addStatic = [0, 0]
click = False

wRookLeft = Rook([0, 7], [0, 0], False, 'Rook')

wRookRight = Rook([7, 7], [0, 0], False, 'Rook')

while not done:
    #Mouse Coordinates
    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    #Size of Window
    SWidth, SHeight = pygame.display.get_surface().get_size()

    screen.fill((255, 255, 255))

    blit('C:\PythonPrograms\Chess\Board.png', 2, 2, 0, 0, 0, 0)

    wRookLeft.show()

    wRookRight.show()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if click:
                click = False
            else:
                click = True

            wRookLeft.move()

            wRookRight.move()

        if event.type == pygame.QUIT or Quit == True:
            done = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            ReSizeHold = False
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)