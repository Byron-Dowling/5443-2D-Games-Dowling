"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

    Asset Credits:
        - Pirate Sprite
            - https://free-game-assets.itch.io/free-2d-pirate-sprites
            - Author: [Free Game Assets] https://free-game-assets.itch.io/ 

        - Background Map Image
            - https://loreobserver.itch.io/customizable-blank-maps
            - Author: [the Lore Observer] https://loreobserver.itch.io/

        - Various Background Theme images
            *Note* Most images were created by me using these items layered together
            - Vecteezy, Author [Grahics RF]
            - https://www.vecteezy.com/vector-art/2978633-walk-the-plank-font-banner-with-pirate-cartoon-character
            - https://www.vecteezy.com/vector-art/3022903-scene-with-wooden-plank-on-the-ship 
            - https://www.vecteezy.com/vector-art/6037135-set-of-pirate-cartoon-characters-and-objects
            - https://www.vecteezy.com/vector-art/5156767-set-of-pirate-cartoon-characters-and-objects
            - https://www.vecteezy.com/vector-art/7190621-empty-ocean-sea-background

            - Vecteezy, Author [Miguel Angel]
            - https://www.vecteezy.com/vector-art/92807-blood-dripping-vectors

            - Vecteezy, Author [tdsouzpro127653]
            - https://www.vecteezy.com/vector-art/12189172-set-of-funny-skulls-white-human-bones-scary-element-of-halloween-death-head-cartoon-flat-illusration

"""

import pygame
import os
import copy
import keyboardlayout as kl
import keyboardlayout.pygame as klp
from DictionaryWords import HMW
from KeyboardMap import ButtonClicked, fetchKey
from PIL import Image, ImageDraw

###################################################################################################

"""
 ██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗
 ██████╔╝███████║██║     █████╔╝ ██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                                                                                      
 ██╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗                             
 ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝                             
 ██║██╔████╔██║███████║██║  ███╗█████╗  ██████╔╝ ╚████╔╝                              
 ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝                               
 ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██║  ██║   ██║                                
 ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝                                


      Helper background class from Dr. Griffin used on Batteship demo                                                                                 
"""

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):

        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.width, self.height = self.getImgWidthHeight(image_file)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (2038, 862))

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


    def getImgWidthHeight(self, path):
        """Uses pil to image size in pixels.
        Params:
            path (string) : path to the image
        """
        if os.path.isfile(path):
            im = Image.open(path)
            return im.size
        return None

###################################################################################################

"""
    Building a Dictionary Lookup of letters and their corresponding image paths
    LetterImages is a current empty list
    LetterImage is our dictionary definition that specifies Letter as the key
    and Image path being the item that it fetches.
"""
LetterImages = []
LetterImage = {"Letter": '', "ImagePath": ""}


"""
    Creating a Dictionary look with keys A - Z where the letter corresponds to
    that letter's image link in my Letters folder.

    Example: When looping through HASH TABLE, we have a list of characters for
    Hash Table and when we loop through them, we'll pull H and it will find the image
    link Letters\L.png and then A will grab A's image from Letters\A.png etc
"""

for x in range(26):
    LetterImage["Letter"] = chr(x+65)
    LetterImage["ImagePath"] = f'Letters\_{LetterImage["Letter"]}.png'
    LetterImages.append(copy.deepcopy(LetterImage))

## Handling the blank spaces and unguess characters
LetterImage["Letter"] = "_"
LetterImage["ImagePath"] = f'Letters\{LetterImage["Letter"]}.png'
LetterImages.append(copy.deepcopy(LetterImage))


###################################################################################################

## Initialize Pygame
pygame.init()

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 800

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Set the title of the window
pygame.display.set_caption("Let's Play Walk the Plank!")

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
BackGround = Background("Vintage_Map.png", [0, 0])

###################################################################################################


"""
 ██╗  ██╗███████╗██╗   ██╗██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
 ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
 █████╔╝ █████╗   ╚████╔╝ ██████╔╝██║   ██║███████║██████╔╝██║  ██║
 ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
 ██║  ██╗███████╗   ██║   ██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
 ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                   
"""

layout_name = kl.LayoutName.QWERTY

# set the letter key size in pixels
key_size = 60
KLC = pygame.Color('black')

# set the keyboard position and color info
keyboard_info = kl.KeyboardInfo(
    position=(0, 500),
    padding=2,
    color=~KLC
)

# set the letter key color, padding, and margin info in px
key_info = kl.KeyInfo(
    margin=10,
    color=KLC,
    txt_color=~KLC,  # invert grey
    txt_font=pygame.font.SysFont('Arial', key_size//4),
    txt_padding=(key_size//6, key_size//10)
)

# set the letter key size info in px
letter_key_size = (key_size, key_size)  # width, height
keyboard_layout = klp.KeyboardLayout(
    layout_name,
    keyboard_info,
    letter_key_size,
    key_info
)

pressed_key_info = kl.KeyInfo(
        margin=14,
        color=pygame.Color('red'),
        txt_color=pygame.Color('white'),
        txt_font=pygame.font.SysFont('Arial', key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
###################################################################################################


## Generate a random word for the ganme iteration from my DictionaryWords file
C4 = HMW()
entry = C4.SelectWord()
print(entry)


###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                             
"""

## Game Control Variables
running = True
winner = True
guessCount = 6              # Total of 6 guesses before game over
correctLetterCount = 0
spriteFrameCount = 0
sharkCount = 1
tick = 0
victimMovement = 0
pirateMovement = 0
guessesRemaing = True
gameOver = False
deathAnimation = False
deathFrameCount = 0

## Run the game loop
while running:

    moveVictim = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            correctGuess = False

            if not gameOver:
                letterGuessed = ButtonClicked(event.pos)

            ## If we have a letter match from the guess, update the bool list
            for i in range(0, len(entry["Letters"]), 1):
                if letterGuessed == entry["Letters"][i]:
                    print("You guessed correctly!")
                    entry["Guessed"][i] = True
                    correctGuess = True
                    correctLetterCount += 1

            ## Ensures guessing the same incorrect letter won't count more than once
            if not correctGuess and letterGuessed != None:
                print("You chose.........poorly")
                guessCount -= 1
                moveVictim = True
                victimMovement += 30

                if not gameOver:
                    pirateMovement += 25

                if guessCount == 0:
                    guessesRemaing = False
                    gameOver = True


    ## "I want you to paint it, paint it, paint it black"
    ## 0,0,0 is default black background
    screen.fill((0,0,0))

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)

    ## Drawing the Keyboard to the screen
    keyboard_layout.draw(screen)

    ## Blank Plank background
    plankBG = pygame.image.load('Plank_bg_sharks.png').convert()
    plankBG = pygame.transform.smoothscale(plankBG, (815,450))
    screen.blit(plankBG, (935,350))

    ## Plank and shark infested water background
    sharks = pygame.image.load(f'Sharks\Shark{sharkCount}.png').convert()
    sharks = pygame.transform.smoothscale(sharks, (815,450))
    screen.blit(sharks,(935,350))


    ## If Game Over
    if gameOver == True:

        ## Ensures the death animation plays once before looping the game over frames
        if deathAnimation == False:
            fallingSprite = pygame.image.load(f'PlankFall\PF{deathFrameCount}.png').convert()
            fallingSprite = pygame.transform.smoothscale(fallingSprite, (815,450))
            screen.blit(fallingSprite,(935,350))

            deathFrameCount += 1

            if deathFrameCount > 23:
                deathAnimation = True

        else:
            ## Plank and shark infested water background
            sharksAndBones = pygame.image.load(f'GameOver\GMO{sharkCount}.png').convert()
            sharksAndBones = pygame.transform.smoothscale(sharksAndBones, (815,450))
            screen.blit(sharksAndBones,(935,350))

    ## Winner screen frames
    if winner == True:
        WBG = pygame.image.load(f'Winner\WBG{sharkCount}.png').convert()
        WBG = pygame.transform.smoothscale(WBG, (815,450))
        screen.blit(WBG,(935,350))


    ## Slow down the animation so the sharks don't swim ridiculously fast
    if tick % 2 == 0:

        sharkCount += 1

        if sharkCount > 8:
            sharkCount = 1


    ## Drawing the Plank victim
    if guessesRemaing == True:
        victimSprite = pygame.image.load(f'Sprites\_Victim_000_IDLE_00{spriteFrameCount}.png')
        victimSprite = pygame.transform.smoothscale(victimSprite, (170, 170))
        screen.blit(victimSprite, (1390 - victimMovement, 485))

    ## Drawing Pirate #1
    pirate1 = pygame.image.load(f'Sprites\_Pirate1_000_IDLE_00{spriteFrameCount}.png')
    pirate1 = pygame.transform.smoothscale(pirate1, (170, 170))
    pirate1Copy = pirate1.copy()
    invertedPirate1 = pygame.transform.flip(pirate1Copy, True, False)
    screen.blit(invertedPirate1, (1445 - pirateMovement, 485))

    ## Drawing Pirate #2
    pirate2 = pygame.image.load(f'Sprites\_Pirate2_000_IDLE_00{spriteFrameCount}.png')
    pirate2 = pygame.transform.smoothscale(pirate2, (170, 170))
    pirate2Copy = pirate2.copy()
    invertedPirate2 = pygame.transform.flip(pirate2Copy, True, False)
    screen.blit(invertedPirate2, (1490, 575))

    ## Most spites run over 6 frames
    spriteFrameCount += 1

    if spriteFrameCount > 6:
        spriteFrameCount = 0

    """
        The idea is to loop through the letters and space them out an even amount
        along the X-axis by incrementing a bias
    """
    xBias = 0
    yBias = 0

    letterCount = len(entry["Letters"])

    ## Loop through our Word's letters and fetch the image links and load the images
    for i in range(0, len(entry["Letters"]), 1):
        if entry["Letters"][i] != " ":
            imgPath = next(item for item in LetterImages if item["Letter"] == entry["Letters"][i])

        if entry["Letters"][i] != " ":

            if entry["Guessed"][i] != False:
                LI = pygame.image.load(imgPath["ImagePath"]).convert()
                LI = pygame.transform.smoothscale(LI, (70,70))
            else:
                winner = False
                LI = pygame.image.load('Letters\_.png').convert()
                LI = pygame.transform.smoothscale(LI, (70,70))

            ## Trying to handle if the words go off the screen so that they appear a row down
            if (xBias - 80) >= screenWidth:
                yBias += 100
                xBias = 0

            screen.blit(LI, (10 + xBias, 50 + yBias))

            xBias += 85

        else:
            letterCount -= 1
            xBias += 85

    if correctLetterCount >= letterCount:
        winner = True

    tick += 1
    pygame.display.update()

###################################################################################################
