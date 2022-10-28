from cmath import log
from dataclasses import dataclass
from turtle import shape, st
import numpy as np

def p(x,y):
    ans=x
    ans/=y
    if(y==0 or x==0):
        return 0
    return ans*(log(ans)/log(2))



data = np.genfromtxt("dataset.csv",delimiter=",", dtype=str)

(row,n)=data.shape

stt=[]
for i in range(1,row):
    stt.append(data[i][n-1])
stt=np.unique(stt)
dcsn=np.zeros(shape=(len(stt)))

t=0
idx=0
for i in range(1,row):
    t+=1
    idx=0
    for kkk in stt:
        if(data[i][n-1]==kkk):
            dcsn[idx]+=1
        idx+=1
idx=0
hfinal=0
for kkk in stt:
    print("p(" + str(kkk) + ")=" + str(dcsn[idx]) + "/" + str(t))
    hfinal-=p(dcsn[idx],t)
    idx+=1

print("H("+str(data[0][n-1])+")="+str(hfinal))

for k in range(0,n-1):

    print("__________ for "+data[0][k]+" row ___________)")
    st=[]
    for i in range(1,row):
        st.append(data[i][k])
    st=np.unique(st)
    h=0
    for kk in st:
        t=0
        stt=[]
        for i in range(1,row):
            stt.append(data[i][n-1])

        stt=np.unique(stt)
        dcsn=np.zeros(shape=(len(stt)))
        idx=0
        ans=0
        for i in range(1,row):
            if(data[i][k]== kk):
                t+=1
                idx=0
                for kkk in stt:
                    if (data[i][n-1]==kkk):
                        dcsn[idx]+=1
                    idx+=1
        
        print("p("+str(kk)+")="+str(t)+"/"+str(row-1))
        idx=0
        for kkk in stt:
            print("p(" +kkk+"|"+ kk+ ")="+ str(dcsn[idx]) + "/"+str(t))
            ans-=p(dcsn[idx],t)
            idx+=1
        
        print("H(" + data[0][n-1] + "|" + data[0][k] +")=" + str(ans))
        h+= ans*(t/(row-1))
        print("")
    print("")
    print ("H("+data[0][k]+")="+str(h))
    print("IG("+data[0][n-1]+"|"+data[0][k]+")=" + str(hfinal-h))
    print("")





