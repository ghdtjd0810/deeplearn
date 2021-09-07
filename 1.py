# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:55:14 2021

@author: LG
"""

from collections import deque

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))
    
# x,y 는 항상 0임. dx,dy는 방향 설정에 도와주는거임
# nx,ny가 결국은 방향을 옮겨주는거에 도움줄거임.
dx = [-1, 1, 0 , 0]
dy = [0,0,-1,1]

# queue 리스트 하나, nx 값 하나 xy값 하나
def bfs(x,y):
    #queue 큐 리스트 하나 만들어보셈
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        #위에 팝하면서 queue에는 아무것도 없는게 되는거고,
        #나중에는 while queue 가 팝하면서 False되면서 while을 빠져나오게됌
        
        #상하좌우를 살피겠다는거임
        #for 0123, 즉 4바퀴돌고 처음에 갔던곳은 pop,
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if nx<0 or ny<0 or nx >= n or ny >= m:
                continue
            
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
                print(graph)
    #지점이 도착하면 끝내버려             
    return graph[n-1][m-1]

print(bfs(0,0))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
