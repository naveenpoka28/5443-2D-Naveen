# CODE YOUR OWN WORDLE IN 60 SECONDS
# import your modules
import random
import pygame
import words
pygame.init()
from pygame import mixer


# create screen, fonts, colors, game variables
white = "#ffffff"
Red = "#FF0000"
black = "#000000"
Green = "#00FF00"
yellow = "#ffff00"
gray = "#808080"
WIDTH, HEIGHT = 1000,800



songloser="Wordle\Assets\loser.mp3"
songwinner="Wordle\Assets\Winner.wav"
song="Wordle\Assets\Music.mp3"
mixer.init()
mixer.music.load(song)
mixer.music.play()


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Wordle 5*6')
turn = 0
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

fps = 60
timer = pygame.time.Clock()
huge_font = pygame.font.Font('Wordle\Assets\Arial.ttf', 56)
normal_text = huge_font.render('Wordle',True,Green)
screen.blit(normal_text,(40,610))
secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
print(secret_word)
game_over = False
letters = 0
turn_active = True

# create routine for drawing the board

def draw_board():
    global turn
    global board
    for col in range(0, 5):
        for row in range(0, 6):
            pygame.draw.rect(screen, black, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)
            piece_text = huge_font.render(board[row][col], True, gray)
            screen.blit(piece_text, (col * 100 + 30, row * 100 + 25))
    pygame.draw.rect(screen, Red, [5, turn * 100 + 5, WIDTH - 10, 90], 3, 5)

# create routine for checking letters

def check_words():
    global turn
    global board
    global secret_word
    for col in range(0, 5):
        for row in range(0, 6):
            if secret_word[col] == board[row][col] and turn > row:
                pygame.draw.rect(screen, Green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
            elif board[row][col] in secret_word and turn > row:
                pygame.draw.rect(screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)



# set up your main game loop

running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    check_words()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# add player controls for letter entry, backspacing, checking guesses and restarting

        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
                entry = event.__getattribute__('text')
                if entry != " ":
                    entry = entry.upper()
                    board[turn][letters] = entry
                    letters += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turn][letters - 1] = ' '
                letters -= 1
            if event.key == pygame.K_RETURN and not game_over:
                turn += 1
                letters = 0
            if event.key == pygame.K_RETURN and game_over:
                turn = 0
                letters = 0
                game_over = False
                secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
                board = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

        # control turn active based on letters
        if letters == 5:
            turn_active = False
        if letters < 5:
            turn_active = True

        # check if guess is correct, add game over conditions

        for row in range(0, 6):
            guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
            if guess == secret_word and row < turn:
                game_over = True

        if turn == 6:
            game_over = True
            loser_text = huge_font.render('LOSER!', True, black)
            screen.blit(loser_text, (40, 610))
  
            mixer.music.stop()          
            mixer.music.load(songloser)
            mixer.music.play()

            

        if game_over and turn < 6:
            winner_text = huge_font.render('WINNER!', True, black)
            screen.blit(winner_text, (40, 610))
            mixer.music.stop()
            mixer.music.load(songwinner)
            mixer.music.play()

            


    pygame.display.flip()
pygame.quit()