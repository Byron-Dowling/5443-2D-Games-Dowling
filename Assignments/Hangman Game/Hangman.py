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
from pygame import mixer
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
 
  ██████╗  █████╗ ███╗   ███╗███████╗        
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝        
 ██║  ███╗███████║██╔████╔██║█████╗          
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝        
                                             
 ███████╗██████╗ ██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝
 ███████╗██████╔╝██████╔╝██║   ██║   █████╗  
 ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  
 ███████║██║     ██║  ██║██║   ██║   ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝
                                             
"""

class GameSprite:
    def __init__(self, imgLink, location, smsc, inverted=False):
        
        if not inverted:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc)
            screen.blit(GS, location)

        else:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc)
            GS_Copy = GS.copy()
            IGS = pygame.transform.flip(GS_Copy, True, False)
            screen.blit(IGS, location)

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

  
"""
    The Wilhelm effect is in the public domain and therefore free from copyright:
    - https://commons.wikimedia.org/wiki/File:Wilhelm_Scream.ogg
"""
mixer.init()
mixer.music.load("Wilhelm_Scream.wav")
mixer.music.set_volume(0.7)

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
                # print(f'Mouse was clicked at {event.pos}')
                letterGuessed = ButtonClicked(event.pos)
                # print(f'You guessed the letter: {letterGuessed}')

            """
                Trying to make the key light up properly but this shitty fucking
                module is so poorly written it doesn't seem to work
            """
            if letterGuessed is not None:
                key = fetchKey(letterGuessed)
                keyboard_layout.update_key(key, pressed_key_info)

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
    plankBG = GameSprite('Plank_bg_sharks.png',(935,350), (815,450), False)


    ## Plank and shark infested water background
    sharks = GameSprite(f'Sharks\Shark{sharkCount}.png',(935,350),(815,450),False)


    ## If Game Over
    if gameOver == True:
        ## Ensures the death animation plays once before looping the game over frames
        if deathAnimation == False:
            fallingSprite = GameSprite(f'PlankFall\PF{deathFrameCount}.png', (935,350), (815,450), False)

            deathFrameCount += 1

            if deathFrameCount > 23:
                deathAnimation = True
                # Start playing the song
                mixer.music.play()

        else:
            ## Plank and shark infested water background
            sharksAndBones = GameSprite(f'GameOver\GMO{sharkCount}.png', (935,350), (815,450), False)

    ## Winner screen frames
    if winner == True:
        WBG = GameSprite(f'Winner\WBG{sharkCount}.png', (935,350), (815,450), False)

    ## Slow down the animation so the sharks don't swim ridiculously fast
    if tick % 2 == 0:
        sharkCount += 1
        if sharkCount > 8:
            sharkCount = 1


    ## Drawing the Plank victim
    if guessesRemaing == True:
        link = f'Sprites\_Victim_000_IDLE_00{spriteFrameCount}.png'
        location = (1390 - victimMovement, 485)
        victimSprite = GameSprite(link, location, (170,170), False)

    ## Drawing Pirate #1
    p1_link = f'Sprites\_Pirate1_000_IDLE_00{spriteFrameCount}.png'
    p1_location = (1445 - pirateMovement, 485)
    pirate1 = GameSprite(p1_link, p1_location, (170,170), True)

    ## Drawing Pirate #2
    p2_link = f'Sprites\_Pirate2_000_IDLE_00{spriteFrameCount}.png'
    p2_location = (1490, 575)
    pirate2 = GameSprite(p2_link, p2_location, (170,170), True)


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
                LI_Link = imgPath["ImagePath"]
                LI_SS = (70,70)
            else:
                winner = False
                LI_Link = 'Letters\_.png'
                LI_SS = (70,70)

            ## Trying to handle if the words go off the screen so that they appear a row down
            if (xBias - 80) >= screenWidth:
                yBias += 100
                xBias = 0

            # screen.blit(LI, (10 + xBias, 50 + yBias))
            LI = GameSprite(LI_Link, (10 + xBias, 50 + yBias), LI_SS, False)

            xBias += 85

        else:
            letterCount -= 1
            xBias += 85

    if correctLetterCount >= letterCount:
        winner = True

    tick += 1
    pygame.display.update()

###################################################################################################
