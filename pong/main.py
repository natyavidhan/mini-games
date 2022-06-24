import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((750, 550))
        pygame.display.set_caption("Pong")

        self.running = True
        self.clock = pygame.time.Clock()
        self.scene = 'home'

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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            if self.scene == 'home':
                self.home()
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()