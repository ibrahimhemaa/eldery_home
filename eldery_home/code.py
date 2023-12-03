import time
from heapq import *
import pygame as pg


class A_Star:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pq = []
        self.par = {}
        self.dx4 = [0, 1, 0, -1]
        self.dy4 = [1, 0, -1, 0]

    def isValid(self, cell):
        return cell[0] >= 0 and cell[0] < self.n and cell[1] >= 0 and cell[1] < self.m

    def heru(self, goal, node):
        return abs(goal[0] - node[0]) + abs(goal[1] - node[1])

    def fit(self, start, goal, move_cost):

        self.pq = []
        self.par = {}
        self.dis = [[1000000000 for _ in range(self.m)] for _ in range(self.n)]
        self.par[start]=-1
        heappush(self.pq, (0, start))
        i, j = start[0], start[1]
        self.dis[i][j] = 0
        while len(self.pq) > 0:
            node = heappop(self.pq)
            # print(f"node-->{node}")
            prev_cost = node[0]
            nodeind = node[1]
            # print(f"nodeind--->{nodeind}")
            for ind in range(4):
                newcell = (nodeind[0] + self.dx4[ind], nodeind[1] + self.dy4[ind])
                # print(f"newcell--->{newcell}")
                if (self.isValid(newcell)):
                    new_cost = prev_cost + self.heru(goal, newcell) + move_cost
                    if (new_cost < self.dis[newcell[0]][newcell[1]]):
                        self.par[newcell] = nodeind
                        self.dis[newcell[0]][newcell[1]] = new_cost
                        heappush(self.pq, (new_cost, newcell))
        return self.dis, self.par


print("enter the size of the house rows * cols ")
n ,m=map(int, input().split())
print("Enter start point i , j")
i ,j=map(int, input().split())
goals = []
i-=1
j-=1
start = (i, j)
print("Enter position of battery room ")
bati , batj = map(int, input().split())
batj-=1
bati-=1
goals.append((bati, batj))
print("Enter position of medicine room ")
medi ,medj =map(int, input().split())
medj-=1
medi-=1
goals.append((medi, medj))
print("Enter number of patients ")
num = int(input())
for i in range(num):
    print(f"Enter position of the {i+1} patient")
    posi ,posj= map(int, input().split())
    posj-=1
    posi-=1
    goals.append((posi, posj))
model = A_Star(n,m)
i = 1
while goals:
    goalnow = goals[0]
    dis,par=model.fit(start,goalnow,1)
    start = goalnow
    print(f"path number {i}")
    print(f"cost to reach goal num {i+1} = {dis[goalnow[0]][goalnow[1]]}")
    i+=1
    while goalnow!=-1:
        print((goalnow[0]+1,goalnow[1]+1))
        goalnow = par[goalnow]
    goals.pop(0)