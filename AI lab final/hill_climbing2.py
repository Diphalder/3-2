def hill_climbing(graph, start):
  current = start
  path = [current]
  global height

  while (1):
    
    if (len(graph[current])==0):
        return path
    

    for adj in graph[current]:
        if(int(height[current])<int(height[adj])):
            neighbor=adj

    current = neighbor
    path.append(current)
  return path

vertex=[]
graph={}
height={}

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

print(hill_climbing(graph, start)) 

"""
4
A 0
B 5
D 20
C 10
4
A B
A C
B D
C D
"""