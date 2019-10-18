import math
global Max,dx
Max=math.pi
dx_list=[0.1,0.01] #h의 값
def f(x): return math.sin(x) #f(x)=sinx
def f_2dx(x): return -math.sin(x)#f''(x)=-sinx

def formula_2(x0,dir): #2점 공식 dir이 -1이면 x0기준 왼쪽 점 이용
    if dir==-1: 
        return (f(x0)-f(x0-dx))/dx
    return (f(x0+dx)-f(x0))/dx
def formula_3(x0): #3점 공식
    return (formula_2(x0,1)-formula_2(x0,-1))/dx
def formula_5(x0): #5점 공식
    return (-f(x0-2*dx)+16*f(x0-dx)-30*f(x0)+16*f(x0+dx)-f(x0+2*dx))/(12*dx*dx)

for i in dx_list: #h의 값을 변화시키면서
    dx=i
    print("h=%f일 때,"%dx)
    x=dx #x는 h부터
    while x+dx<=Max: #Max-h값까지
        ans=f_2dx(x) #f''(x)의 값과
        if x-2*dx<0 or x+2*dx>Max:#수치해석적으로 구한 2차 미분값을 비교
            formula=formula_3(x)
            print("x=%f, f''(x)=%f, 3점공식f''(x)=%f, 오차=%f"%(x,ans,formula,ans-formula))
        else:
            formula=formula_5(x)
            print("x=%f, f''(x)=%f, 5점공식f''(x)=%f, 오차=%f"%(x,ans,formula,ans-formula))
        x=x+dx
    
