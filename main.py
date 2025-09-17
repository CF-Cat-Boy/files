import pygame
import random

def game():
    global running
    def gameover(score):
        global running
        print(f"Score: {score}")
        running = False

    class Head(object):
        def __init__(self):
            self.rect = pygame.Rect(64, 64, 32, 32)
            self.score = 0
            self.body = []
            self.dir = 3 # possible vals are: 1, 3, 5, 7
        def move(self):
            if self.dir > 3:
                self.rect.y += (self.dir-6)*32
            else:
                self.rect.x += (self.dir-2)*32
            for i in self.body:
                if self.rect.colliderect(i.rect) and not i.id == 0:
                    gameover(self.score)
            if self.rect.x > screen.get_width() or self.rect.x < 0:
                gameover(self.score)
                #self.rect.x = abs((self.rect.x)-608)+32
            elif self.rect.y > screen.get_height() or self.rect.y < 0:
                gameover(self.score)
                #self.rect.y = abs((self.rect.y)-608)+32
                
                
                
                
        def eat(self):
            self.body.append(Body([self.rect.x,self.rect.y], self.body.__len__()))
            self.score += 1
            
    class Body(object):
        def __init__(self, pos, id):
            self.rect = pygame.Rect(pos[0]+4, pos[1]+4, 24, 24)
            self.id = id
        def move(self, xy):
            self.rect.x = xy[0]+4
            self.rect.y = xy[1]+4
    
    class Apple(object):
        def __init__(self):
            self.rect = pygame.Rect((random.randint(1,(screen.get_width()//32)-1)*32)+4, (random.randint(1,(screen.get_height()//32)-1)*32)+4, 24, 24)
        def ate(self):
            self.rect.x = (random.randint(1,(screen.get_width()//32)-1)*32)+4
            self.rect.y = (random.randint(1,(screen.get_height()//32)-1)*32)+4

    h = 0

    # Initialise pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((0,0))

    clock = pygame.time.Clock()
    head = Head()
    apple = Apple()
    prevdirs = []

    quitt = False
    running = True
    while running:
        
        h += 1

        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            if head.dir <= 3:
                head.dir = 5
        elif key[pygame.K_a] or key[pygame.K_LEFT]:
            if head.dir > 3:
                head.dir = 1
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            if head.dir <= 3:
                head.dir = 7
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            if head.dir > 3:
                head.dir = 3

        if key[pygame.K_ESCAPE]:
            quitt = True
            running = False

        if head.rect.colliderect(apple.rect):
            head.eat()
            apple.ate()
        
        if h%15==0:
            prevdirs.append((head.rect.x, head.rect.y))
            if prevdirs.__len__() > head.body.__len__():
                prevdirs.pop(0)
            head.move()
            for i in range(head.body.__len__()):
                head.body[i].move(prevdirs[i])

        # display
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), head.rect)
        for i in head.body:
            pygame.draw.rect(screen, (255, 255, 255), i.rect)
        pygame.draw.rect(screen, "#d61431", apple.rect)
        pygame.display.flip()
    if not quitt:
        game()
game()
pygame.quit()