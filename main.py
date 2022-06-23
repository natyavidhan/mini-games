import pygame

class Cell:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x*10
        self.y = y*10
        self.widht = 10
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.widht, self.height)
        self.typ = 0 # 0 = dead, 1 = alive

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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
            self.screen.fill((0, 0, 0))

            if pygame.mouse.get_pressed()[0]:
                coord = pygame.mouse.get_pos()
                x = coord[0] - coord[0] % 10
                x = coord[1] - coord[1] % 10
                print(x, y)

            for y in self.grid:
                for x in y:
                    r = x.rect
                    if x.typ == 0:
                        pygame.draw.rect(self.screen, (0, 0, 0), r)
                    else:
                        pygame.draw.rect(self.screen, (255, 255, 255), r)

            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()