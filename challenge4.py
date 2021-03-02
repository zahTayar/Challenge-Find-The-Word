import pygame
import random
import sys

pygame.init()
# set colors
black = (0, 0, 0)
red = (128, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
purple = (128, 0, 128)
light_purple = (255, 0, 255)
light_red = (255, 0, 0)
light_green = (0, 255, 0)
light_blue = (0, 0, 255)

# set screen size
screenS_width = 800
screenS_height = 600
screenS_game = 500

# set font
smallFont = pygame.font.SysFont("Arial", 20)
medFont = pygame.font.SysFont("Arial", 45)
largeFont = pygame.font.SysFont("Arial", 55)

# set window with title
game = pygame.display.set_mode((screenS_width, screenS_height))
pygame.display.set_caption("Challenge-4")

# frame per second
fps = pygame.time.Clock()

#class to choose random word from words.txt

class randomWord:
    def __init__(self):
        self.wordList = []
        self.posLis = []

    def readWordsFromFile(self, fileName):
        try:
            with open(fileName, "r") as f:
                for line in f:
                    self.wordList.append(line)
        except:
            print(f'Something Went Wrong')

    def randomWordForGame(self):
        location = random.randint(0, len(self.wordList))
        word = self.wordList[location]
        for i in range(len(word) - 1):
            self.posLis.append(0)
        return word
#checks if there is a letter that the user didnt saw , working on array of zeros .
    def searchZero(self, word):
        for i in range(len(word) - 1):
            if self.posLis[i] == 0:
                return i

    def getCharFromWord(self, word):
        loca = random.randint(0, len(word) - 2)
        if self.posLis[loca] > 0:
            index = self.searchZero(word)
            self.posLis[index] = 1
            return word[index]
        else:
            self.posLis[loca] = 1
            return word[loca]

#split word to chars
def split1(text):
    return [char for char in text]

#check if the randomword is even to the player word.
def checkThem(text, word):
    if len(text) != len(word):
        return False
    li = split1(text)
    lu = split1(word)
    for i in range(len(li)):
        if li[i] != lu[i]:
            return False
    return True

#winner screen
def winnerscreen():
    win1 = pygame.display.set_mode((screenS_game, screenS_game))
    while True:
        win1.fill(white)
        messageToScreen("flag{Winner_Winner_Chicken_Dinner}", black, -150, -80, size="small")
        button("Quit", 150, 300, 150, 50, light_red, red, action="quit")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver()

#retry screen
def retryScreen(score, word, liChars):
    input_box = pygame.Rect(220, 290, 140, 32)
    text = ''
    text1 = ""
    active = True
    afterRe = False
    color = green
    while True:
        game.fill(white)
        messageToScreen("Game Over !!", black, -150, -250, size="medium")
        messageToScreen("score: " + str(score), black, -150, -200, size="small")
        messageToScreen("Your Randomaly Chars: ", black, -150, -170, size="small")
        button("Retry", 0, 450, 150, 50, light_purple, purple, action="retry")
        button("Quit", 350, 450, 150, 50, light_red, red, action="quit")
        for i in range(len(liChars)):
            messageToScreen(str(liChars[i]) + ",", black, -300 + (i * 15), -150, size="small")
        messageToScreen("You think you know the answer??? ", black, -150, -120, size="small")
        if len(word) == len(liChars):
            messageToScreen("You got all the chars", black, -150, -100, size="small")
        if not afterRe:
            messageToScreen("Enter password:", black, -250, 0, size="small")
            pygame.draw.rect(game, color, input_box, 2)
        else:
            text1 = text1 + '\n'

            if checkThem(text1, word):
                winnerscreen()
            else:
                messageToScreen("Error ,you can do better don't give up, jajajaj", red, -150, -80, size="small")
        txt_surface = pygame.font.Font(None, 32).render(text, True, black)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        game.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            color = light_green if active else green
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        afterRe = True
                        text1 = text
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

#start screen with the story
def startScreen():
    while True:
        game.fill(white)
        messageToScreen("The Untold Story About Harry Potter", red, 0, -250, size="large")
        button("Start", 100, 500, 150, 50, light_purple, purple, action="start")

        messageToScreen("You think that you have what it takes ? jajaja ", black, 0, -180, size="small")
        messageToScreen("This challenge is not like the others ,consider it as a promise. ", black, 0, -150,
                        size="small")
        messageToScreen("But remember Harry counts on you", black, 0, -120, size="small")
        messageToScreen("Harry was after the battle with lord Voldemort and he was tired . ", black, 0, -90,
                        size="small")
        messageToScreen("He just wanted a good meal and some sleep, but he knew his duty,To destroy the", black, 0, -60,
                        size="small")
        messageToScreen("wand of Voldemort. But when he touches it ,something strange happened.", black, 0, -30,
                        size="small")
        messageToScreen("He get stuck in a room that full of snakes and the only way out", black, 0, 0, size="small")
        messageToScreen("is to beat the snakes and get the password . He need your help.", black, 0, 30, size="small")
        messageToScreen("All you have is the arrows and your ability to think.", black, 0,
                        60, size="small")
        messageToScreen("Remember, after pushing start or retry , the game will choose a different random word .", black, 0,
                        90, size="small")
        messageToScreen("Every bite is worth a char (but randomly char)", black, 0,
                        120, size="small")
        messageToScreen("Just promise me that you'll be careful , one touch in the border and you are done.  ", black, 0,
                        150, size="small")

        messageToScreen("Enjoy, Author: Zackuel", green, 0, 210, size="small")
        button("Quit", 550, 500, 150, 50, light_red, red, action="quit")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver()


def startplay(fps1):
    liChars = []
    r = randomWord()
    ch = ''
    r.readWordsFromFile("words.txt")
    word = r.randomWordForGame()
    print(word)
    win = pygame.display.set_mode((screenS_game, screenS_game))
    score = 0
    snake = Snake()
    foodsp = FoodSp()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.changeDirTo("LEFT")
                if event.key == pygame.K_RIGHT:
                    snake.changeDirTo("RIGHT")
                if event.key == pygame.K_DOWN:
                    snake.changeDirTo("DOWN")
                if event.key == pygame.K_UP:
                    snake.changeDirTo("UP")

        foodPos = foodsp.spawnFood()
        if snake.move(foodPos):
            score += 1
            if score <= 12:
                ch = r.getCharFromWord(word)
                liChars.append(ch)
            # we need to print char
            foodsp.setFoodOnSc(False)
        win.fill(white)
        for pos in snake.getbody():
            pygame.draw.rect(win, red, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(win, green, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
        if snake.checkCollision():
            retryScreen(score, word, liChars)
        pygame.display.set_caption("Challenge-4 |char :" + str(ch) + " | score: " + str(score))

        pygame.display.flip()
        fps.tick(fps1)


# create buttons and design them and there place , and take care in case of action

def button(text, x, y, width, height, inactiveColor, activeColor, textColor=black, action=None):
    currentPos = pygame.mouse.get_pos()
    isPressed = pygame.mouse.get_pressed()

    if x + width > currentPos[0] > x and y + height > currentPos[1] > y:
        pygame.draw.rect(game, activeColor, (x, y, width, height))
        if isPressed[0] == 1 and action != None:
            if action == "quit":
                gameOver()
            if action == "start":
                startplay(33)
            if action == "retry":
                startplay(33)
    else:
        pygame.draw.rect(game, inactiveColor, (x, y, width, height))
    text_to_button(text, textColor, x, y, width, height)


# write text on the button
def text_to_button(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurface, textRec = text_objects(msg, color, size)
    textRec.center = (buttonX + (int(buttonWidth / 2)), buttonY + (int(buttonHeight / 2)))
    game.blit(textSurface, textRec)


# print a message on the screen
def messageToScreen(msg, color, x_displace=0, y_displace=0, size="small"):
    textSurface, textRec = text_objects(msg, color, size)
    textRec.center = ((int(screenS_width / 2)) + x_displace, y_displace + (int(screenS_height / 2)))
    game.blit(textSurface, textRec)


def text_objects(text, color, size):
    if size == "small":
        textS = smallFont.render(text, True, color)
    elif size == "medium":
        textS = medFont.render(text, True, color)
    elif size == "large":
        textS = largeFont.render(text, True, color)

    return textS, textS.get_rect()


# game over
def gameOver():
    pygame.quit()
    sys.exit()


#######snake game######
class Snake:
    def __init__(self):  # initial the first pos as (100,50),body size 3 , Right direction on start
        self.pos = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.dir = "RIGHT"
        self.chaDir = self.dir

    # change direction ,and check if user do something illegal , like going right and press left (illegal)
    def changeDirTo(self, dir1):
        if dir1 == "RIGHT" and not self.dir == "LEFT":
            self.dir = "RIGHT"
        if dir1 == "LEFT" and not self.dir == "RIGHT":
            self.dir = "LEFT"
        if dir1 == "UP" and not self.dir == "DOWN":
            self.dir = "UP"
        if dir1 == "DOWN" and not self.dir == "UP":
            self.dir = "DOWN"

    # move- chang the position by adding or substract 10 from (x,y),if you see food the grow
    def move(self, foodpos):
        if self.dir == "RIGHT":
            self.pos[0] += 10
        if self.dir == "LEFT":
            self.pos[0] -= 10
        if self.dir == "UP":
            self.pos[1] -= 10
        if self.dir == "DOWN":
            self.pos[1] += 10
        self.body.insert(0, list(self.pos))
        if self.pos == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    # check in case of collision(hit the bounderies)->dead
    def checkCollision(self):
        if self.pos[0] > 490 or self.pos[0] < 0:
            return 1
        if self.pos[1] > 490 or self.pos[1] < 0:
            return 1
        for bodypart in self.body[1:]:
            if self.pos == bodypart:
                return 1
        return 0

    def getpos(self):
        return self.pos

    def getbody(self):
        return self.body


##############Food###############
class FoodSp:
    def __init__(self):  # set the food as a random place ,flag
        self.foodposit = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isFoodOnSc = True

    def spawnFood(self):
        if not self.isFoodOnSc:
            self.foodposit = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.isFoodOnSc = True
        return self.foodposit

    def setFoodOnSc(self, B):
        self.isFoodOnSc = B


if __name__ == "__main__":
    startScreen()
