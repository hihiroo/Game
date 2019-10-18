import math as m
global Max,dx
Max=m.pi*2
dx=0.01
def f(x): return 1/x #f(x)=1/x
def f_dx(x): return -1/(x*x)
def formula_2(x0): #2점 공식
    if x0+dx>Max: 
        return (f(x0)-f(x0-dx))/dx
    return (f(x0+dx)-f(x0))/dx
def formula_3(x0): #3점 공식
    return (f(x0+dx)-f(x0-dx))/(2*dx)
def formula_5(x0): #5점 공식
    return (8*(f(x+dx)-f(x-dx))-(f(x+2*dx)-f(x-2*dx)))/(12*dx)
def j(n,x):
    return m.pow(-1,n)*m.pow(x,n)*m.pow(f_dx(x),n)*m.sin(x)/x
def numerical_j(n,x,formula): #수치해석적 미분으로 1/x를 미분하여 j(x)구하기
    if formula==5:
        return m.pow(-1,n)*m.pow(x,n)*m.pow(formula_5(x),n)*m.sin(x)/x
    elif formula==3:
        return m.pow(-1,n)*m.pow(x,n)*m.pow(formula_3(x),n)*m.sin(x)/x
    else:
        return m.pow(-1,n)*m.pow(x,n)*m.pow(formula_2(x),n)*m.sin(x)/x

x=dx
while x<=Max:
    if x-2*dx<=0 or x+2*dx>Max:# 5점 공식 사용못할 때 
        if x-dx==0 or x+dx>Max: # 2점 공식
            ans1=numerical_j(1,x,2)
            ans2=numerical_j(2,x,2)
        else: #3점 공식
            ans1=numerical_j(1,x,3)
            ans2=numerical_j(2,x,3)
    else:
        ans1=numerical_j(1,x,5)
        ans2=numerical_j(2,x,5)
    print("x=%f, j1(x)=%f, 오차:%f, j2(x)=%f, 오차:%f"%(x,ans1,j(1,x)-ans1,ans2,j(2,x)-ans2))
    x=x+dx










