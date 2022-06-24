import pygame
import time

pygame.init()
pygame.font.init()

class Cell:
    def __init__(self, index, x, y, alive=False):
        self.index = index
        self.x = x*10
        self.y = y*10
        self.widht = 10
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.widht, self.height)
        self.alive = alive

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((750, 600))
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.clock = pygame.time.Clock()
        self.grid = self.gen_grid()
        self.simulate = False
    
    def gen_grid(self):
        grid = []
        index = 0
        for y in range(55):
            grid.append([])
            for x in range(75):
                grid[y].append(Cell(index, x, y))
                index+=1
        return grid

    def display_info(self):
        surface = pygame.Surface((750, 50))
        surface.fill((0, 0, 0))

        pygame.draw.line(surface, (255, 255, 255), (0, 0), (750, 0), 5)

        font = pygame.font.SysFont("comicsans", 20)
        instruction_1 = font.render("Press Space to Start Simulation", True, (255, 255, 255))
        instruction_2 = font.render("Press Right key to simulate next step", True, (255, 255, 255))

        ins_rect_1 = instruction_1.get_rect()
        ins_rect_1.x, ins_rect_1.y = 10, 3

        ins_rect_2 = instruction_2.get_rect()
        ins_rect_2.x, ins_rect_2.y = 10, 20

        surface.blit(instruction_1, ins_rect_1)
        surface.blit(instruction_2, ins_rect_2)

        pygame.draw.line(surface, (255, 255, 255), (375, 0), (375, 50), 2)
        sim = "Running" if self.simulate else "Paused"

        sim_text = pygame.font.SysFont("comicsans", 32).render(f"Simulation: {sim}", True, (255, 255, 255))
        sim_text_rect = sim_text.get_rect()
        sim_text_rect.x, sim_text_rect.y = 385, 3
        surface.blit(sim_text, sim_text_rect)

        self.screen.blit(surface, (0, 550))

    def update(self):
        for y in self.grid:
            for x in y:
                r = x.rect
                if x.alive:
                    pygame.draw.rect(self.screen, (255, 255, 255), r)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), r)
        pygame.display.update()
    
    def simulation(self):
        new_grid = self.gen_grid()
        index = 0
        for y in range(55):
            for x in range(75):
                cell = self.grid[y][x]
                neighbours = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        e = (y+i+55)%55
                        f = (x+j+75)%75
                        if self.grid[e][f].alive:
                            neighbours+=1
                if cell.alive:
                    neighbours-=1
                if not cell.alive and neighbours ==3:
                    new_grid[y][x] = Cell(index, x, y, True)
                elif (neighbours < 2 or neighbours > 3):
                    if cell.alive:
                        new_grid[y][x] = Cell(index, x, y)
                else:
                    new_grid[y][x] = cell
                index += 1
        self.grid = new_grid


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.simulate = not self.simulate
                        time.sleep(0.5)
                    elif event.key == pygame.K_RIGHT:
                        self.simulation()
                        time.sleep(0.2)

            if pygame.mouse.get_pressed()[0]:
                coord = pygame.mouse.get_pos()
                x = coord[0] // 10
                y = coord[1] // 10
                self.grid[y][x].alive = not self.grid[y][x].alive
                self.update()
                time.sleep(0.2)

            self.display_info()
            self.clock.tick(30)
            self.update()
            if self.simulate:
                self.simulation()

if __name__ == "__main__":
    game = Game()
    game.run()