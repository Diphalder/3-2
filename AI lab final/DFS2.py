import numpy as np

stk=[]

def dfs(u):
    global visit
    global graph
    stk.append(u)
    visit[u]=1
    while(len(stk)!=0):
        u=stk.pop()
        print(u,end="->")
        for v in graph[u]:
            if(visit[v]==0):
                stk.append(v)
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

print("DFS sequence = [ ",end="")
dfs(start)
print(" ] ")

