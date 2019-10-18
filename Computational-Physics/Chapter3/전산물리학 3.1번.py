import math
global Max,dx
Max=math.pi
dx_list=[0.1,0.01] #h의 값
def f(x): return math.sin(x) #f(x)=sinx
def f_dx(x): return math.cos(x)#f'(x)=cosx

def formula_2(x0): #2점 공식
    if x0+dx>Max: 
        return (f(x0)-f(x0-dx))/dx
    return (f(x0+dx)-f(x0))/dx
def formula_3(x0): #3점 공식
    return (f(x0+dx)-f(x0-dx))/(2*dx)
def formula_5(x0): #5점 공식
    return (8*(f(x+dx)-f(x-dx))-(f(x+2*dx)-f(x-2*dx)))/(12*dx)

for i in dx_list: #h의 값을 변화시키면서
    dx=i
    print("h=%f일 때,"%dx)
    x=0 #x는 0부터
    while x<=Max: #Max값까지
        ans=f_dx(x) #f'(x)의 값과
        if x-2*dx<0 or x+2*dx>Max:#수치해석적으로 구한 1차 미분값을 비교
            if x==0 or x+dx>Max:
                formula=formula_2(x)
                print("x=%f, f'(x)=%f, 2점공식f'(x)=%f, 오차=%f"%(x,ans,formula,ans-formula))
            else:
                formula=formula_3(x)
                print("x=%f, f'(x)=%f, 3점공식f'(x)=%f, 오차=%f"%(x,ans,formula,ans-formula))
        else:
            formula=formula_5(x)
            print("x=%f, f'(x)=%f, 5점공식f'(x)=%f, 오차=%f"%(x,ans,formula,ans-formula))
        x=x+dx
