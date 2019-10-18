#문제: y' + ysinx = y^2sinx (단, x=0일때 y=1/2이다.)
import math as m

initial_x=0 #초기 x값=0
initial_y=1/2 #초기 y값=0 
h=0.01 #x값의 변위
last_x=2 # [0,2]에서 구함


def f(x,y): # y'=f(x,y)
    return m.pow(y,2)*m.sin(x)-y*m.sin(x)


def ans_y(x): #해석적 해
    return 1/(1+m.e**(-m.cos(x)+1))

    
def Euler(x,y):#수치해석적 해
    if x>=last_x:
        return 0 #x값이 구간 넘으면 종료
    
    next_y=y+f(x,y)*h #y(x+h)
    ans=ans_y(x+h) #해석적 해
    
    print("Euler_y(%.2f)=%f. 해석적_y(%.2f)=%f\n"%(x+h,next_y,x+h,ans))
    print('_'*10,"오차는 %f\n"%(ans-next_y))
    
    return Euler(x+h,next_y)


print("y(%.2f)=%.2f"%(initial_x,initial_y))
Euler(initial_x,initial_y)
