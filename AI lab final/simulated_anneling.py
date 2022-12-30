path=[]
maxpath=[]
def hill_climbing(graph, cur):
   
    global height
    global maxpath
    global maxheigth
    global path
    path.append(cur)
    f=1
    for adj in graph[cur]:
        if(int(height[cur])<=int(height[adj])):
            hill_climbing(graph,adj)
            f=0
    if(f):
        x=int(height[cur])
        if(maxheigth<x):
            maxheigth=x
            maxpath.clear()
            for i in path:
                maxpath.append(i)


    path.pop()    


vertex=[]
graph={}
height={}
maxheigth=0



n=int(input("enter number of vertex: "))

for i in range(n):
    z=input()
    x,h=z.split()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        height[x]=h


n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)



start=input("enter start node : ")

hill_climbing(graph, start)

print(maxheigth)
print(maxpath)


"""
6
A 0
B 5
D 20
C 10
E 3
F 30
7
A B
A C
B D
C D
D E
B F
F D
"""