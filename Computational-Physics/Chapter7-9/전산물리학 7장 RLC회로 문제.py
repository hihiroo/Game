R=1
L=1
C=0.5
dt=0.01
Max=10

def Euler(i,q):
    
    Euler_i=i-dt*(R*i+q/C)/L #전류 I(t+dt)구하기
    Euler_q=q+i*dt #전하량 Q(t+dt) 구하기

    print("t=%f, I=%f, Q=%f"%(t,i,q))
    return [Euler_i,Euler_q] # 리스트 반환

t=0
next=[-1,5]
while t<=Max:
    next=Euler(next[0],next[1]) #리스트 0번=I, 리스트 1번=q
    t=t+dt
    


     
 
