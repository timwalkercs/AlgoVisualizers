
import pygame
import math
from queue import PriorityQueue

#Start of Prog

#Set dimensions of the grid
HEIGHT = 800
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH+200, HEIGHT))
#Set caption
pygame.display.set_caption("Path Finding Visualizer")

#Store several color values
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (153, 204, 255)
YELLOW = (255, 255, 102)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
PURPLE = (127, 0, 255)
PINK = (255, 204, 204)

#Node class
class Node:
    #Node initialzation
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE #Nodes are initialized to be white
        self.neighbors = []
        self.width = width #square Node's width/height
        self.total_rows = total_rows

    #method to locate a Node
    def locate(self):
        return self.row, self.col

    #methods to query state of a Node
    def is_closed(self):
        return self.color == BLUE

    def is_open(self):
        return self.color == YELLOW

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == GREEN

    def is_end(self):
        return self.color == RED

    def is_path(self):
        return self.color == PINK

    #methods to set state of a Node
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = BLUE
    
    def make_open(self):
        self.color = YELLOW

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED
    
    def make_path(self):
        self.color = PINK

    #draw the actual Node in the window
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    #update Node's neighbors
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #Down
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #Up
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #Left
            self.neighbors.append(grid[self.row][self.col-1])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #Right
            self.neighbors.append(grid[self.row][self.col+1])

    def __lt__(self, other):
        return False

#define the hueristic function
def hVal(p1, p2):
    #extract x and y coords from each point
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def drawPath(parent_dict, crnt, draw):
    while crnt in parent_dict:
        crnt = parent_dict[crnt]
        crnt.make_path()
        draw()


#A* algorithm
def astar(draw, grid, start, end, hueristic):
    draw()

    count = 0 #tracks order of nodes put in fringe

    fringe = PriorityQueue()
    fringe.put((0, count, start))

    parent_dict = {} #designates what node came from where

    #define f and g values for start node
    gVal = {node: float("inf") for row in grid for node in row} #cost of path from start to given Node, default inf.
    gVal[start] = 0 
    fVal = {node: float("inf") for row in grid for node in row}
    fVal[start] = hVal(start.locate(), end.locate())

    fringe_hash = {start}

    while not fringe.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        
        crnt = fringe.get()[2]
        fringe_hash.remove(crnt)

        if crnt==end: #Path found
            drawPath(parent_dict, end, draw)
            print("SUCCESS")
            return True

        for neighbor in crnt.neighbors:
            temp_gVal = gVal[crnt] + 1
            if temp_gVal < gVal[neighbor]: #if current path is better
                parent_dict[neighbor] = crnt #set crnt to be parent of the neighbor
                gVal[neighbor] = temp_gVal #set gVal of neighbor

                if hueristic:
                    fVal[neighbor] = temp_gVal + hVal(neighbor.locate(), end.locate()) #set fVal of neighbor
                else: #Dijkstra's algorithm
                    fVal[neighbor] = temp_gVal
                    
                if neighbor not in fringe_hash:
                    count += 1
                    fringe.put((fVal[neighbor], count, neighbor)) #add neighbor to fringe for exploration
                    fringe_hash.add(neighbor)
                    neighbor.make_open() #mark neighbor as open (to be explored)
        
        draw()

        if crnt != start and crnt != end: crnt.make_closed() #close the explored Node

    print("Path Not Found!")
    return None

#create data structure for the grid of Nodes
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            if i==0 or j==0 or i==rows-1 or j==rows-1:
                node.make_barrier()
            grid[i].append(node)

    return grid

#draw grid lines that separate the Nodes
def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows+1):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows+1):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

#draw the entire display
def draw(win, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid_lines(win, rows, width)
    pygame.display.update()

#given mouse position, translate it to grid coords of a Node
def get_click_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

#Button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        

def main(win, width):
    win.fill(WHITE)
    ROWS = 50
    COLS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    running = True
    started = False

    #set up images to be used as buttons
    abutton_image = pygame.image.load('astarbutton.png').convert_alpha()
    clearbutton_image = pygame.image.load('clearbutton.png').convert_alpha()
    dbutton_image = pygame.image.load('dijkstrabutton.png').convert_alpha()
    clearButton = Button(825, 50, clearbutton_image)
    aButton = Button(825, 125, abutton_image)
    dButton = Button(825, 175, dbutton_image)

    while running:
        draw(win, grid, ROWS, WIDTH)
        clearButton.draw()
        aButton.draw()
        dButton.draw()

        #handle events while program is still running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if started: #algorithm started
                continue
            
            if pygame.mouse.get_pressed()[0]: #left click
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    node = grid[row][col]

                    if not start and node != end: #place start Node
                        start = node
                        start.make_start()

                    elif not end and node != start: #place end Node
                        end = node
                        end.make_end()

                    elif node != start and node != end: #if node isn't start or end -> make barrier
                        node.make_barrier()
                       

            elif pygame.mouse.get_pressed()[2]: #right click
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    node = grid[row][col]

                    if node.is_barrier() and (0<row<ROWS-1) and (0<col<ROWS-1): #if Node is barrier
                        node.reset()
                    elif node.is_open() or node.is_closed() or node.is_path():
                        node.reset()

            elif pygame.mouse.get_pressed()[1]: #middle click
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    node = grid[row][col]

                    if node.is_barrier(): #if Node is barrier
                        print("Barrier")
                    elif end!=None:
                        print(hVal(node.locate(), end.locate()))

            elif event.type == pygame.MOUSEBUTTONUP: #checks button clicks
                pos = pygame.mouse.get_pos()
                x, y = pos
                if 825<x<975 and 50<y<90:
                    print("Clear")
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                elif 825<x<975 and 125<y<165:
                    print("A*")
                    if not started:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        
                        astar(lambda: draw(win, grid, ROWS, width), grid, start, end, True)
                        start.make_start()
                        end.make_end()

                elif 825<x<975 and 175<y<215:
                    print("Dijkstra's")
                    if not started:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        
                        astar(lambda: draw(win, grid, ROWS, width), grid, start, end, False)
                        start.make_start()
                        end.make_end()



    pygame.quit()

main(WIN, WIDTH)
