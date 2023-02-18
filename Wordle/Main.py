# importing game modules
import random
import pygame
import words
pygame.init()

# creating font, colors and size of the screen
WIDTH , HEIGHT= 500, 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('Arial.ttf', 50)

black = "#000000"
blue = "#CCFFFF"
green = "#006400"
yellow = "#FFFF00"
red = "#FF0000"

pygame.display.set_caption('Wordel Game')
t = 0
window = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]


hidden_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
game_over = False
word = 0
game_running = True



#code for creating table on the output window
def draw_window():
    global t
    global window
    for col in range(0, 5):
        for row in range(0, 6):
            pygame.draw.rect(screen, blue, [col * 100 +12, row * 100 +12, 75, 75], 90, 90)
            piece_text = font.render(window[row][col], True, red)
            screen.blit(piece_text, (col * 100 + 30, row * 100 + 25))
    pygame.draw.rect(screen, red, [7, t * 100 + 7, WIDTH - 10, 90], 8, 8)

# adding hidden word into the game

def check_words():
    global t
    global window
    global hidden_word
    for col in range(0, 5):
        for row in range(0, 6):
            if hidden_word[col] == window[row][col] and t > row:
                pygame.draw.rect(screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
            elif window[row][col] in hidden_word and t > row:
                pygame.draw.rect(screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)

# set up your main game loop

running = True
while running:
    screen.fill(black)
    check_words()
    draw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# creating player controls by using different keyboard keys

        if event.type == pygame.TEXTINPUT and game_running and not game_over:
                e = event.__getattribute__('text')
                if e != " ":
                    e = e.upper()
                    window[t][word] = e
                    word += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and word > 0:
                window[t][word - 1] = ' '
                word -= 1
            if event.key == pygame.K_RETURN and not game_over:
                t += 1
                word = 0
            if event.key == pygame.K_RETURN and game_over:
                t = 0
                word = 0
                game_over = False
                hidden_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
                window = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

        if word == 5:
            game_running = False
        else:
            game_running = True

        # code to check if the entered word is correct

        for row in range(0, 6):
            guess = window[row][0] + window[row][1] + window[row][2] + window[row][3] + window[row][4]
            if guess == hidden_word and row < t:
                game_over = True

    pygame.display.flip()
pygame.quit()