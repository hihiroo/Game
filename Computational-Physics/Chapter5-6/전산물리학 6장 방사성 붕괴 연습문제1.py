from matplotlib import pyplot as p
import numpy as np
import math as m

#초기조건
Max=100000 #t구간 [0,Max)
dt=10000
Half_Life_Period_A=5013
Half_Life_Period_B=138376

#그래프 배열 생성
t=np.array(np.arange(0,Max,dt)) #t축 정의역-> 0부터 Max까지 dt간격으로
A=np.array(np.arange(0,Max,dt))
B=np.array(np.arange(0,Max,dt))
C=np.array(np.arange(0,Max,dt))

la=m.log(2)/Half_Life_Period_A
lb=m.log(2)/Half_Life_Period_B
A[0]=1.0e5
B[0]=0
C[0]=0

def dNA(nA): #t에 의존하지않음.  
    return -la*nA
def dNB(nA,nB):
    return la*nA-lb*nB
def dNC(nB): 
    return lb*nB

def NA(index):
    if index*dt>=Max:
        return 0
    
    A[index]=A[index-1]+dt*dNA(A[index-1])
    
    return NA(index+1)

def NB(index):
    if index*dt>=Max:
        return 0
    
    B[index]=B[index-1]+dt*dNB(A[index-1],B[index-1])

    return NB(index+1)

def NC(index):
    if index*dt>=Max:
        return 0
    
    C[index]=C[index-1]+dt*dNC(B[index-1]) 
    return NC(index+1)


NA(1)
NB(1)
NC(1)
p.plot(t,A,label="A")
p.plot(t,B,linestyle="--",label="B")
p.plot(t,C,'r',label="C")
p.legend()
p.show()

    

