#문제: v'(t)=-g-k*v(t)/m
#질량 m=0.01kg, 마찰계수 k=0.05kg/s, 중력가속도 g=9.8m/s^2, 초기속도 v0=20m/s
import math

g=9.8
m=0.01
k=0.05
v0=20
h=0.01 #t값의 변위
last_t=2 # [0,2]에서 구함


def f(t,v): # v'=f(t,v)
    return -g-k*v/m


def ans_v(t): #해석적 해
    return (v0+m*g/k)*math.e**(-k*t/m)-m*g/k

    
def Euler(t,v):#수치해석적 해
    if t>=last_t:
        return 0 #t값이 구간 넘으면 종료
    
    next_v=v+f(t,v)*h #v(t+h)
    ans=ans_v(t+h) #해석적 해
    
    print("Euler_v(%.2f)=%.4fm/s.  해석적_v(%.2f)=%.4fm/s\n"%(t+h,next_v,t+h,ans))
    print('_'*10,"오차는 %f\n"%(ans-next_v))
    
    return Euler(t+h,next_v)


print("v(%d)=%dm/s"%(0,v0))
Euler(0,v0)
