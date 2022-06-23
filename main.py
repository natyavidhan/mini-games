import pygame
import time

class Cell:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x*10
        self.y = y*10
        self.widht = 10
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.widht, self.height)
        self.alive = False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((750, 550))
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()
        self.grid = []
        index = 0
        for y in range(55):
            self.grid.append([])
            for x in range(75):
                self.grid[y].append(Cell(index, x, y))
                index+=1
    
    def update(self):
        for y in self.grid:
            for x in y:
                r = x.rect
                if x.alive:
                    pygame.draw.rect(self.screen, (255, 255, 255), r)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), r)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
            self.screen.fill((0, 0, 0))

            if pygame.mouse.get_pressed()[0]:
                coord = pygame.mouse.get_pos()
                x = coord[0] // 10
                y = coord[1] // 10
                self.grid[y][x].alive = not self.grid[y][x].alive
                self.update()
                time.sleep(0.5)

            self.clock.tick(60)
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run()