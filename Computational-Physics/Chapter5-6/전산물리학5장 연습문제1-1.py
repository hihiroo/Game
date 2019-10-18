#문제: y' + y/x = 1 - x^2 (단, x=1일때 y=1이다.)
import math

initial_x=1
initial_y=1
h=0.01
last_x=2

def f(x,y):
    return 1-math.pow(x,2)-y/x

def ans_y(x): #해석적 해
    return (1/2)*x-(1/4)*math.pow(x,3)+(3/4)/x
    
def Euler(x,y):
    if x>=last_x:
        return 0
    next_y=y+f(x,y)*h
    ans=ans_y(x+h)
    print("Euler_y(%.2f)=%f. 해석적_y(%.2f)=%f\n"%(x+h,next_y,x+h,ans))
    print('_'*10,"오차는 %f\n"%(ans-next_y))
    return Euler(x+h,next_y)

print("y(%d)=%d"%(initial_x,initial_y))
Euler(initial_x,initial_y)
