import numpy as np

q=[]

def bfs(u):
    global visit
    global graph
    q.append(u)
    visit[u]=1
    while(len(q)!=0):
        u=q.pop(0)
        print(u,end=",")
        for v in graph[u]:
            if(visit[v]==0):
                q.append(v)
                visit[v]=1
    
vertex=[]
graph={}
visit={}

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        visit[x]=0

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)


start=vertex[0]

print("BFS sequence = [ ",end="")
bfs(start)
print(" ] ")

"""
7
S
A
B
C
D
E
G
8
S A
S B
S C
A D
A E
A G
B G
C G
"""