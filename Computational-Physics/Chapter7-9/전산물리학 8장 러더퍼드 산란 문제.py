import math
from matplotlib import pyplot as p
import numpy as np

#unit define
AMU=1.66*10**-27
charge_unit=1.6*10**-19

#initial condition
m_alpha=4*AMU #질량
m_target=197*AMU

Q_alpha=2*charge_unit #전하량
Q_target=79*charge_unit

k=8.99*10**9 #쿨롱 상수
R=197**(0.33333)*(10**-15) #과녁핵 반지름

dt=10**-23 #계산하는 시간 간격
Max_t=4*10**-20 #여기까지 계산


#두 점 사이의 거리 구하는 함수
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#가속도 구하는 함수
def accel(target_xy,alpha_xy,r_):
    u=Q_alpha*k*Q_target/m_alpha #상수로 처리
    x=(alpha_xy[0]-target_xy[0])*u/(r_**3)
    y=(alpha_xy[1]-target_xy[1])*u/(r_**3)
    return [x,y]

color=['r','y','g','b'] #초기 알파입자 y좌표 따라 다르게 색 표시하기 위해
cnt=0 #y좌표 다르게 몇 개 만들었는지 알기 위해

for alpha_initial_y in np.array(np.arange(R/2,R*10,R)):#초기 알파입자 y좌표를 다양하게 설정

    #initial condition
    alpha_x=[-2*10**-13] #알파입자 초기x좌표
    alpha_y=[alpha_initial_y] #알파입자 초기 y좌표
    alpha_v=[10**7,0] #알파입자 초기 속도[x,y]
    target_x=0 #과녁핵 초기 x좌표
    target_y=0
    target_v=[0,0] #과녁핵 초기 속도
    time=0

    
    while time<Max_t:
        index=len(alpha_x)

        
        #알파입자 이동 위치(Euler방법) 
        alpha_x.append(alpha_x[index-1]+dt*alpha_v[0])
        alpha_y.append(alpha_y[index-1]+dt*alpha_v[1])
        

        #과녁핵 이동위치
        target_x=target_x+dt*target_v[0]
        target_y=target_y+dt*target_v[1]


        #알파입자&과녁핵 사이 거리
        r=distance(alpha_x[index],alpha_y[index],target_x,target_y)
        

        #가속도
        if r>R: #알파입자가 과녁핵 바깥에 있는 경우
            alpha_a=accel([target_x,target_y],[alpha_x[index],alpha_y[index]],r)
            
        else: #알파입자가 과녁핵 안에 있는 경우
            alpha_a=accel([target_x,target_y],[alpha_x[index],alpha_y[index]],R)
        
        target_a=[-alpha_a[0]*m_alpha/m_target,-alpha_a[1]*m_alpha/m_target]
        

        #속도
        alpha_v=[alpha_v[0]+dt*alpha_a[0],alpha_v[1]+dt*alpha_a[1]]
        target_v=[target_v[0]+dt*target_a[0],target_v[1]+dt*target_a[1]]
        
        
        time=time+dt



    #그래프 그리기
    p.plot(alpha_x,alpha_y,color[cnt%4])
    p.xticks(np.arange(-2*10**-13,4*10**-14,4*10**-14)) #x축 간격 조정
    p.yticks(np.arange(0,30*10**-14,5*10**-14)) #y축 간격 조정
    
    cnt=cnt+1
    
p.show()
