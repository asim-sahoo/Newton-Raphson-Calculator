import sympy as sp
import time

fun = input("Enter function:")
x0 = float(input("Enter initial approximation:"))
e = float(1e-5)

x = sp.Symbol('x')
exp = sp.sympify(fun) 
dydx = exp.diff() 

f = sp.lambdify(x, exp)
df = sp.lambdify(x, dydx)

xi_1 = x0
st=time.time()
while True:
    if df(xi_1) == 0.0:
        print("Divide by zero error")
        break
    xi = xi_1 - f(xi_1)/df(xi_1)
    print("x =",xi,"f(x) =",f(xi))
    if abs(xi - xi_1) < e:
        break
    xi_1 = xi
et=time.time()
print("Runtime:",et-st)    
print("So the approximate root is :",xi)