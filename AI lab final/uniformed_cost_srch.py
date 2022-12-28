import numpy as np

from queue import PriorityQueue
q=PriorityQueue()

def bfs(u,ed):
    global visit
    global graph
    global costt
    global totalcost
    global q
    q.put((0,u))
    visit[u]=1
    while(q.empty!=1):
        cost,u=q.get()
        print(u,end="->")
        if(u==ed):
            return
        for v in graph[u]:
            if(visit[v]==0):
                cost=costt[(u,v)]
                totalcost[v]=totalcost[u]+int(cost)
                q.put((totalcost[v],v))
                visit[v]=1
    
vertex=[]
graph={}
visit={}
totalcost={}
costt={}

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        visit[x]=0
        totalcost[x]=0


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

