import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((750, 550))
        pygame.display.set_caption("Pong")

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))

            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()