import numpy as np

from queue import PriorityQueue
q=PriorityQueue()


path=[]
par={}
def bfs(u,ed):
    global visit
    global graph
    global costt
    global totalcost
    global q
    global pathcost
    q.put((0,u))
    visit[u]=1
    totalcost[u]=0
    while(q.empty!=1):
        cost,u=q.get()
        print(u,end=",")
        if(u==ed):
            pathcost=min(pathcost,totalcost[u])
            return
        for v in graph[u]:
            if(visit[v]==0):
                cost=costt[(u,v)]
                totalcost[v]=min(totalcost[u]+int(cost),totalcost[v])
                par[v]=u
                q.put((totalcost[v],v))
                visit[v]=1
    
vertex=[]
graph={}
visit={}
totalcost={}
costt={}

pathcost=100000000000000

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        visit[x]=0
        totalcost[x]=100000000000000
        par[x]=None


n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v,cost= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)
        costt[(u,v)]=cost



start=input("enter start node : ")
end =input("enter end node : ")

#print(graph)

print("Uniformed sequence = [ ",end="")
bfs(start,end)
print(" ] ")

print("path cost = ", pathcost)


v=end
path=[]
while v is not None:
    path.append(v)
    v=par[v]
path.reverse()
print("the path is = ",  path)

"""
9
S
A
B
C
D
E
F
G
H
10
S A 5
S B 2
S C 4
A D 9
A E 4
B G 6
C F 2
E G 6
F G 2
D H 7
"""