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
    def __init__(self, position, moved, lifted, piece, color, alive):
        self.pos = position #position of piece on board
        self.mov = moved #position of piece when being lifted and moved
        self.lif = lifted #piece is lifted or not
        self.piece = piece #type of piece
        self.color = color #color of piece
        self.alive = alive #piece alive?

    def move(self): #for moving the piece

        global placing

        if square(Mouse_x, Mouse_y) == [self.pos[0], self.pos[1]] and click: #if mouse is on same square as piece and mouse is clicked
            global addStatic
            global current #didn't take me half an hour to figure out current was a global variable
            addStatic = [Mouse_x, Mouse_y] #anchor for adding value to piece position
            current = self.piece #piece currently being moved in str() form
            self.lif = True #piece is lifted
            board[tuple(square(Mouse_x, Mouse_y))] = 0
            placing = True #i dont know wut i did but its working so dont touch it

        if self.lif and not click: #piece is put down
            if square(Mouse_x, Mouse_y) in self.light():
                if board[tuple(square(Mouse_x, Mouse_y))]:
                    board[tuple(square(Mouse_x, Mouse_y))].kill() #kills piece (duh)
                    
                self.pos[0] = square(Mouse_x, Mouse_y)[0]
                self.pos[1] = square(Mouse_x, Mouse_y)[1] #center piece on square
                board[tuple(square(Mouse_x, Mouse_y))] = eval(self.piece)
            else:
                board[tuple(self.pos)] = eval(self.piece)

            self.lif = False #piece is not lifted anymoar
            current = 0

    def kill(self):
        self.alive = False

class Rook(Actor): #Rook (duh)
    def show(self): #blits image
        if self.lif:
            add[0] = Mouse_x - addStatic[0]
            add[1] = Mouse_y - addStatic[1]
            blit('C:\PythonPrograms\Chess\{0}.png'.format(self.piece), 1.2, 1.065, self.pos[0], self.pos[1], add[0], add[1])
        else:
            blit('C:\PythonPrograms\Chess\{0}.png'.format(self.piece), 1.2, 1.065, self.pos[0], self.pos[1], 0, 0)

    def light(self): #no longer lights up squares but too efficient (lazy) to change the name

        light = [] #squares to be lit

        for i in range(self.pos[0]): #squares to left
            if not board[tuple([self.pos[0] - 1 - i, self.pos[1]])]:
                light.append([self.pos[0] - 1 - i, self.pos[1]])
            else:
                if self.color == board[tuple([self.pos[0] - 1 - i, self.pos[1]])].color:
                    break
                else:
                    light.append([self.pos[0] - 1 - i, self.pos[1]])
                    break

        for i in range(7 - self.pos[0]): #squares to right
            if not board[tuple([self.pos[0] + 1 + i, self.pos[1]])]:
                light.append([self.pos[0] + 1 + i, self.pos[1]])
            else:
                if self.color == board[tuple([self.pos[0] + 1 + i, self.pos[1]])].color:
                    break
                else:
                    light.append([self.pos[0] + 1 + i, self.pos[1]])
                    break

        for j in range(self.pos[1]): #sqaures above (down)
            if not board[tuple([self.pos[0], self.pos[1] - 1 - j])]:
                light.append([self.pos[0], self.pos[1] - 1 - j])
            else:
                if self.color == board[tuple([self.pos[0], self.pos[1] - 1 - j])].color:
                    break
                else:
                    light.append([self.pos[0], self.pos[1] - 1 - j])
                    break
        
        for j in range(7 - self.pos[1]): #sqaures below (up)
            if not board[tuple([self.pos[0], self.pos[1] + 1 + j])]:
                light.append([self.pos[0], self.pos[1] + 1 + j])
            else:
                if self.color == board[tuple([self.pos[0], self.pos[1] + 1 + j])].color:
                    break
                else:
                    light.append([self.pos[0], self.pos[1] + 1 + j])
                    break

        return light

screen = pygame.display.set_mode((900, 750), pygame.RESIZABLE)
img = pygame.image.load('C:\PythonPrograms\Chess\ImageCalibrator1.png').convert()
pressed = pygame.key.get_pressed()
done = False
Quit = False
add = [0, 0]
addStatic = [0, 0]
click = False
current = 0
placing = False
light = []

#1 == 'white'; 0 == 'black';
wRookLeft = Rook([0, 7], [0, 0], False, 'wRookLeft', 1, True)
wRookRight = Rook([7, 7], [0, 0], False, 'wRookRight', 1, True)
bRookLeft = Rook([0, 0], [0, 0], False, 'bRookLeft', 0, True)
bRookRight = Rook([7, 0], [0, 0], False, 'bRookRight', 0, True)

pieces = [
    wRookLeft,
    wRookRight,
    bRookLeft,
    bRookRight,
]

board = {}

for i in range(8):
    for j in range(8):
        board[(i, j)] = 0

for piece in pieces:
    board[tuple(piece.pos)] = piece

while not done:
    #Mouse Coordinates
    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    #Size of Window
    SWidth, SHeight = pygame.display.get_surface().get_size()

    screen.fill((255, 255, 255))

    blit('C:\PythonPrograms\Chess\Board.png', 2, 2, 0, 0, 0, 0)

    for piece in pieces:
        if piece.alive:
            piece.show()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[tuple(square(Mouse_x, Mouse_y))] or placing:
                if click:
                    click = False
                else:
                    click = True

                placing = False

            if board[tuple(square(Mouse_x, Mouse_y))]:
                board[tuple(square(Mouse_x, Mouse_y))].move()

            if current:
                eval(current).move()

        if event.type == pygame.QUIT or Quit == True:
            done = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            ReSizeHold = False
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)