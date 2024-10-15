import pygame
from time import sleep, time
def fall():
        global falling
        global speedx
        global speedy
        global running   
def getttlvl():
    global lvlnum
    global quitt
    global lvlcomp
getttlvl()
global lvlnum
global lvlcomp
lvlcomp = False
lvlnum = 1
def game():
    getttlvl()
    global lvlnum
    global quitt
    global lvlcomp
    lvlcomp = False
    quitt = False
    jumpforce = -10
    gravity = 2
    speedm = 2.5
    resistance = 0.75

    # Class for the orange dude
    class Player(object):
        def __init__(self):
            self.rect = pygame.Rect(64, 64, 24, 24)

        def move(self, dx, dy):
            
            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)
        
        def move_single_axis(self, dx, dy):

            fall()
            global falling
            global speedx
            global speedy
            global running
            getttlvl()
            global lvlnum
            global quitt
            global lvlcomp

            # Move the rect
            if not (self.rect.x + dx) >= 1080 and not (self.rect.x + dx) <= 0:
                self.rect.x += dx
            if not (self.rect.y + dy) >= 720 and not (self.rect.y + dy) <= 0:
                self.rect.y += dy
            if (self.rect.x + dx) >= 1080 or (self.rect.x + dx) <= 0:
                speedx = 0
            if (self.rect.y + dy) >= 720 or (self.rect.y + dy) <= 0:
                speedy = 0

            # If you collide with a wall, move out based on velocity
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
            for wall in scaffs:
                if self.rect.colliderect(wall.rect):
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
            for wall in iscaffs:
                if self.rect.colliderect(wall.rect):
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
            '''for wall in lscaffs:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
            for wall in rscaffs:
                if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0'''
            for badwall in badwalls:
                if self.rect.colliderect(badwall.rect) and badwall.solid :
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = badwall.rect.left
                        speedx = 0
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = badwall.rect.right
                        speedx = 0
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = badwall.rect.top
                        speedy = 0
                        falling = 0
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = badwall.rect.bottom
                        speedy = 0
                    badwall.stable = False
            if self.rect.colliderect(end_rect):
                running = False
                if not lvlnum == 4:
                    if lvlcomp == False:
                        lvlcomp = True
                        lvlnum += 1
                        self.move(100, 100)
                        if lvlnum == 4:
                            quitt = True
            for kill in kills:
                if self.rect.colliderect(kill.rect):
                    running = False
            for killi in killis:
                if self.rect.colliderect(killi.rect):
                    running = False
            for left in lefts:
                if self.rect.colliderect(left.rect):
                    speedx -= 1
            for right in rights:
                if self.rect.colliderect(right.rect):
                    speedx += 1
            for up in ups:
                if self.rect.colliderect(up.rect):
                    speedy += -2
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.move_single_axis(0, -1)

    # Nice class to hold a wall rect
    class Wall(object):
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Kill(object):
        def __init__(self, pos):
            kills.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Killi(object):
        def __init__(self, pos):
            killis.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Left(object):
        def __init__(self, pos):
            lefts.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Right(object):
        def __init__(self, pos):
            rights.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Up(object):
        def __init__(self, pos):
            ups.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class FakeWall(object):
        def __init__(self, pos):
            fakewalls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class BadWall(object):
        def __init__(self, pos):
            self.solid = True
            self.stable = True
            self.t1 = float
            self.t2 = float
            self.tt1 = False
            self.tt2 = False
            badwalls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Scaff(object):
        def __init__(self, pos):
            scaffs.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 8)
    class IScaff(object):
        def __init__(self, pos):
            iscaffs.append(self)
            self.rect = pygame.Rect(pos[0], pos[1]+24, 32, 8)
    '''class LScaff(object):
        def __init__(self, pos):
            lscaffs.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 8, 32)
    class RScaff(object):
        def __init__(self, pos):
            rscaffs.append(self)
            self.rect = pygame.Rect(pos[0]+24, pos[1], 8, 32)'''

    def badwallloop():
        for badwall in badwalls:
            if not badwall.stable:
                if not badwall.tt1:
                        badwall.t1 = time()
                        badwall.tt1 = True
                if time()-badwall.t1 > 0.5:
                    badwall.solid = False
                    if not badwall.tt2:
                        badwall.t2 = time()
                        badwall.tt2 = True
                    if time()-badwall.t2 > 5:
                        badwall.solid = True
                        badwall.stable = True
                        badwall.tt2 = False
                        badwall.tt1 = False


    fall()
    global falling
    global speedx
    global speedy
    global running
    falling = 0
    speedx = 0
    speedy = 0
    running = False        

    # Initialise pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1080, 720))

    clock = pygame.time.Clock()
    kills = []
    lefts = []
    rights = []
    ups = []
    walls = [] # List to hold the walls
    badwalls = []
    fakewalls = []
    scaffs = []
    iscaffs = []
    lscaffs = []
    rscaffs = []
    killis = []
    player = Player() # Create the player
    def lvl(num):
        test = [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                 ⚑dd",
        "██████████████████████████████████",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  "
        ]
        lvl1 = [
        "                ████              ",
        "                ▓▓▓▓              ",
        "                ████              ",
        "                                 ⚑",
        "██████   ████  ██ █ █  █  █   █ ██",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ]
        lvl2 = [
        "█    █████████████████████████████",
        "█    █                           █",
        "█    █                           █",
        "█    █⚑                          █",
        "█    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███-█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    ████████                   ^█",
        "█    ▓>>>>>>>                   ^█",
        "█    ████████                   ^█",
        "█    <<<<<<<<                   ^█",
        "██████████████████████████████████"
        ]
        lvl3 = [
        "                                  ",
        "                                  ",
        "                                  ",
        "███████████████████████████       ",
        "                            ^^^^^^",
        "                           ^^^^^^^",
        "                           ^^^^^^^",
        "     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "     █XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "                                  ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "                                  ",
        "                                  ",
        "   ⚑                              ",
        "██████████████████████████████████",
        "                                  ",
        "                                  "
        ]

        if num == 0:
            return test
        if num == 1:
            return lvl1
        if num == 2:
            return lvl2
        if num == 3:
            return lvl3
    x = y = 0
    print(lvlnum)
    for row in lvl(lvlnum):
        for col in row:
            if col == "█":
                Wall((x, y))
            if col == "▓":
                FakeWall((x, y))
            if col == "⚑":
                end_rect = pygame.Rect(x, y, 32, 32)
            if col == "X":
                Kill((x, y))
            if col == "x":
                Killi((x, y))
            if col == "<":
                Left((x, y))
            if col == ">":
                Right((x, y))
            if col == "▒":
                BadWall((x, y))
            if col == "-":
                Scaff((x, y))
            if col == "_":
                IScaff((x, y))
            '''if col == "[":
                LScaff((x, y))
            if col == "]":
                RScaff((x, y))'''
            if col == "^":
                Up((x, y))
            x += 32
        y += 32
        x = 0

    running = True
    while running:
        
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        badwallloop()

        # Move the player if the space,a,d/up,left,right keys are pressed
        falling = falling+1
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            speedx = speedx-speedm
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            speedx = speedx+speedm
        if key[pygame.K_F11]:
            if clock.tick(10)/2:
                pygame.display.toggle_fullscreen()
        if key[pygame.K_SPACE] or key[pygame.K_UP]:
            if falling < 3:
                speedy = speedy+jumpforce
        if key[pygame.K_ESCAPE]:
            quitt = True
            running = False

        
        speedx = speedx*resistance
        speedy = speedy+gravity 
        player.move(speedx, speedy)
        
        #print(speedx, speedy, falling)   
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        for fakewall in fakewalls:
            pygame.draw.rect(screen, (250, 250, 250), fakewall.rect)
        for kill in kills:
            pygame.draw.rect(screen, (255, 0, 0), kill.rect)
        for left in lefts:
            pygame.draw.rect(screen, (128, 128, 255), left.rect)
        for right in rights:
            pygame.draw.rect(screen, (255, 200, 0), right.rect)
        for up in ups:
            pygame.draw.rect(screen, (255, 0, 255), up.rect)
        for badwall in badwalls:
            if badwall.solid:
                pygame.draw.rect(screen, (128, 128, 128), badwall.rect)
        for scaff in scaffs:
            pygame.draw.rect(screen, (188, 106, 60), scaff.rect)
        for iscaff in iscaffs:
            pygame.draw.rect(screen, (188, 106, 60), iscaff.rect)
        for lscaff in lscaffs:
            pygame.draw.rect(screen, (188, 106, 60), lscaff.rect)
        for rscaff in rscaffs:
            pygame.draw.rect(screen, (188, 106, 60), rscaff.rect)
        pygame.draw.rect(screen, (0, 255, 0), end_rect)
        pygame.draw.rect(screen, (255, 128, 128), player.rect)
        pygame.display.flip()
    if quitt == False:
        game()
game()
pygame.quit()