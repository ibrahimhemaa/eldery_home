# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
import time
from heapq import *
import pygame as pg
def heuristic(a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_neighbours(x, y):
    check_neighbour = lambda x, y: True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]#, [-1, -1], [1, -1], [1, 1], [-1, 1]
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_neighbour(x + dx, y + dy)]
def A_star(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}
    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break
        neighbours = graph[cur_node]
        for neighbour in neighbours:
            neigh_cost, neigh_node = neighbour
            new_cost = cost_visited[cur_node] + neigh_cost
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited
from heapq import *
def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4
def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2
cols, rows = 23, 13
TILE = 70
pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
grid = [
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
    '11111111111111111111111',
]
grid = [[int(char) for char in string ] for string in grid]
grid[11][20]=9
grid[1][11]=9
grid[2][2]=9
grid[10][4]=9
grid[5][12]=9
grid[11][15]=9
grid[8][21]=9
grid[2][21]=9
graph={}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_neighbours(x, y)
bg = pg.image.load('js.png').convert()
bg = pg.transform.scale(bg, (cols * TILE, rows * TILE))
start = (0, 7)
goal = start
queue = []
vec=((20,11),(11,1),(2,2),(4,10),(12,5),(15,11),(21,8),(21,2))
i=0
cost_visited = {start: 0}
visited = {start: None}
heappush(queue, (0, start))
while i!=8:
    sc.blit(bg, (0, 0))
    mouse_pos =vec[i]
    if mouse_pos:
        visited=A_star(start,mouse_pos,graph)
        goal=mouse_pos
    path_head, path_segment = goal, goal
    while path_segment and path_segment in visited:
        pg.draw.circle(sc, pg.Color('blue'), *get_circle(*path_segment))
        path_segment = visited[path_segment]
    pg.draw.circle(sc, pg.Color('red'), *get_circle(*start))
    pg.draw.circle(sc, pg.Color('magenta'), *get_circle(*path_head))
    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    time.sleep(2)
    start = goal
    goal = start
    i+=1
    clock.tick(30)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
