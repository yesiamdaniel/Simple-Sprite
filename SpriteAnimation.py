import pygame
import os

#
# # import pygame module in this program
# import pygame
#
# # activate the pygame library
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # define the RGB value for white,
# #  green, blue colour .
# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
#
# # assigning values to X and Y variable
# X = 400
# Y = 400
#
# # create the display surface object
# # of specific dimension..e(X, Y).
# display_surface = pygame.display.set_mode((X, Y))
#
# # set the pygame window name
# pygame.display.set_caption('Show Text')
#
# # create a font object.
# # 1st parameter is the font file
# # which is present in pygame.
# # 2nd parameter is size of the font
# font = pygame.font.Font('freesansbold.ttf', 32)
#
# # create a text suface object,
# # on which text is drawn on it.
# text = font.render('GeeksForGeeks', True, green, blue)
#
# # create a rectangular object for the
# # text surface object
# textRect = text.get_rect()
# print(textRect)
#
# # set the center of the rectangular object.
# textRect.center = (X // 2, Y // 2)
# print(textRect)
#
# # infinite loop
# while True:
#
#     # completely fill the surface object
#     # with white color
#     display_surface.fill(white)
#
#     # copying the text surface object
#     # to the display surface object
#     # at the center coordinate.
#     display_surface.blit(text, textRect)
#
#     # iterate over the list of Event objects
#     # that was returned by pygame.event.get() method.
#     for event in pygame.event.get():
#
#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT:
#             # deactivates the pygame library
#             pygame.quit()
#
#             # quit the program.
#             quit()
#
#             # Draws the surface object to the screen.
#         pygame.display.update()

# Inital Params
pygame.init()
clock = pygame.time.Clock()
win_width = 500
win_height = 480
win = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
bg = pygame.image.load('media/bg.jpg')
pygame.display.set_caption("first game")
score = 0


bulletsound = pygame.mixer.Sound('media\\bullet.wav')
hitsound = pygame.mixer.Sound('media\\hit.wav')

music = pygame.mixer.music.load('media\\music.mp3')
pygame.mixer.music.play(-1)


class Player:
    char = pygame.image.load('media\\standing.png')
    walkLeft = [pygame.image.load('media\\L1.png'),
                pygame.image.load("media\\L2.png"),
                pygame.image.load('media\\L3.png'),
                pygame.image.load("media\\L4.png"),
                pygame.image.load("media\\L5.png"),
                pygame.image.load("media\\L6.png"),
                pygame.image.load("media\\L7.png"),
                pygame.image.load("media\\L8.png"),
                pygame.image.load("media\\L9.png")]
    walkRight = [pygame.image.load('media\\R1.png'),
                 pygame.image.load("media\\R2.png"),
                 pygame.image.load('media\\R3.png'),
                 pygame.image.load("media\\R4.png"),
                 pygame.image.load("media\\R5.png"),
                 pygame.image.load("media\\R6.png"),
                 pygame.image.load("media\\R7.png"),
                 pygame.image.load("media\\R8.png"),
                 pygame.image.load("media\\R9.png")]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.IsJump = False
        self.JumpCount = 10
        self.left = True
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.walkcount + 1 >= 18:
            self.walkcount = 0

        if not self.standing:
            if self.left:
                win.blit(man.walkLeft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(man.walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                win.blit(man.walkRight[0], (self.x, self.y))
            else:
                win.blit(man.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 18, self.y + 12, 28, 50)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        # pygame.draw.rect(win, (0, 0, 255), (x - width, y, width, height), 8)
        # pygame.draw.rect(win, (0, 0, 255), (x, y, width, height), 8)
        # pygame.draw.circle(win, (255, 0, 0), (x, y), 30, 8)

    def hit(self):
        self.IsJump = False
        self.JumpCount = 10
        self.x = 60
        self.y = 410
        self.walkcount = 0
        global score
        score -= 1
        font = pygame.font.SysFont('arial', 28)
        text = font.render("PLAYER HIT -1", True, (255, 0, 0))
        rect = text.get_rect()
        rect.center = (win_width // 2, win_height // 2)
        win.blit(text, rect)
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


class Enemy:
    walkLeft = [pygame.image.load('media\\L1E.png'),
                pygame.image.load("media\\L2E.png"),
                pygame.image.load('media\\L3E.png'),
                pygame.image.load("media\\L4E.png"),
                pygame.image.load("media\\L5E.png"),
                pygame.image.load("media\\L6E.png"),
                pygame.image.load("media\\L7E.png"),
                pygame.image.load("media\\L8E.png"),
                pygame.image.load("media\\L9E.png"),
                pygame.image.load("media\\L10E.png"),
                pygame.image.load("media\\L11E.png")]

    walkRight = [pygame.image.load('media\\R1E.png'),
                 pygame.image.load("media\\R2E.png"),
                 pygame.image.load('media\\R3E.png'),
                 pygame.image.load("media\\R4E.png"),
                 pygame.image.load("media\\R5E.png"),
                 pygame.image.load("media\\R6E.png"),
                 pygame.image.load("media\\R7E.png"),
                 pygame.image.load("media\\R8E.png"),
                 pygame.image.load("media\\R9E.png"),
                 pygame.image.load("media\\R10E.png"),
                 pygame.image.load("media\\R11E.png")
                 ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.hegiht = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.hitcount = 0
        self.health = 10
        self.visible = True

    def draw(self):
        if self.visible:
            self.move()
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount // 4], (self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkLeft[self.walkcount // 4], (self.x, self.y))
                self.walkcount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 5 * self.health, 10))
            self.hitbox = (self.x + 20, self.y, 28, 60)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
            hitsound.play()
            self.hitcount += 1
            global score
            score += 1
        else:
            self.visible = False



class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Text:
    @staticmethod
    def print_text():
        font = pygame.font.SysFont('arial', 28, bold=True)  # Returns font object
        text = font.render(f'Score: {score}', True, (0, 0, 255), (33, 142, 215))  # Returns surface object
        rect = text.get_rect()
        rect.center = 400, 30
        win.blit(text, rect)


def redrawgamewindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw()
    Text.print_text()

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []
shootLoop = 0

# MAIN LOOP
run = True

while run:
    clock.tick(40)

    if goblin.visible == True:
        # Collision Handler
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] \
                and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] \
                and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()

    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        # C
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] \
                and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] \
                    and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
        if win_width > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_1]:
    #    Text().print_text()

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletsound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(
                Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < win_width - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkcount = 0

    if not man.IsJump:
        # if keys[pygame.K_UP] and y > 0:
        #   y -= vel
        # if keys[pygame.K_DOWN] and y < win_height - height:
        #   y += vel
        if keys[pygame.K_UP]:
            man.IsJump = True
            man.right = False
            man.left = False
            man.walkcount = 0
    elif man.JumpCount >= -10:
        neg = 1
        if man.JumpCount < 0:
            neg = -1
        man.y -= int((man.JumpCount ** 2) * 0.5 * neg)
        man.JumpCount -= 1
    else:
        man.IsJump = False
        man.JumpCount = 10

    redrawgamewindow()

pygame.quit()
