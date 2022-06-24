import pygame

class Paddle:
    def __init__(self, left=True):
        self.width = 25
        self.height = 100
        self.x = 30 if left else 720 - self.width
        self.y = 275 - (self.height/2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self):
        self.radius = 5
        self.x = 375 - self.radius
        self.y = 275 - self.radius

        self.xVel = 15
        self.yVel = 15

        self.rect = pygame.Rect(self.x, self.y, self.radius*2, self.radius*2)
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.radius*2, self.radius*2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((750, 550))
        pygame.display.set_caption("Pong")

        self.running = True
        self.clock = pygame.time.Clock()
        self.scene = 'home'

        self.score = [0, 0]
        self.speed = 10
        
        self.player_1 = Paddle()
        self.player_2 = Paddle(False)
        self.ball = Ball()

    def home(self):
        img = pygame.image.load("home.png")
        self.screen.blit(img, (0, 0))

        btn_1 = pygame.Rect(250, 295, 250, 70)
        btn_2 = pygame.Rect(250, 380, 250, 70)

        if pygame.mouse.get_pressed()[0]:
            if btn_1.collidepoint(pygame.mouse.get_pos()):
                self.scene = 'pvp'
            if btn_2.collidepoint(pygame.mouse.get_pos()):
                self.scene = 'pvc'
    
    def player_vs_player(self):
        self.screen.blit(pygame.image.load("playground.png"), (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.player_1.y-self.speed >= 0:
            self.player_1.y-=self.speed
        if keys[pygame.K_s] and self.player_1.y+self.speed+self.player_1.height <= 550:
            self.player_1.y+=self.speed
        if keys[pygame.K_UP] and self.player_2.y-self.speed >= 0:
            self.player_2.y-=self.speed
        if keys[pygame.K_DOWN] and self.player_2.y+self.speed+self.player_2.height <= 550:
            self.player_2.y+=self.speed

        self.player_1.update()
        self.player_2.update()

        pygame.draw.rect(self.screen, (114, 115, 53), self.player_1.rect)
        pygame.draw.rect(self.screen, (114, 115, 53), self.player_2.rect)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            if self.scene == 'home':
                self.home()
            if self.scene == 'pvp':
                self.player_vs_player()
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()