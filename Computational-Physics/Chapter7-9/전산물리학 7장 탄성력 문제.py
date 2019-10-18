#시간의 변화에 따른 물체의 변위, 속도, 가속도를 구하는 프로그램

m=1 #질량 
k=1 #용수철 상수
c=0.5 #마찰 상수 
x=1 #물체의 초기 위치
v=0 #물체의 초기 속도

dt=0.1 #0.1초 간격으로 계산
maxt=20 #20초까지 계산

def F(x,v): #F(x,v)=합력, -kx=탄성력, -cv=마찰력
    return -k*x-c*v

t=0
while t<maxt:
    a=F(x,v)/m #가속도
    x=x+v*dt #위치
    v=v+a*dt #속도
    print("t=%f, x=%f, v=%f, a=%f"%(t,x,v,a))
    t=t+dt
