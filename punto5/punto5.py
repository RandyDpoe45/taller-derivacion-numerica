from sympy import *
import numpy as np

def der2(x1,h):
    x=Symbol('x')
    f=x*(np.e**x)
    res=N(f.subs({x:x1+h}))
    res2=N(f.subs({x:x1}))
    return ((res-res2)/h)
    
def main():
    x=Symbol('x')
    f=diff(x*(np.e**x),x)
    e=f.subs({x:1})
    for i in range(1,17):
        r=der2(1,1/(10**i))
        print("|"+str(e)+"|"+str(1/(10**i))+"|"+str(r)+"|"+str(abs(e-r))+"|")
        
if __name__ == "__main__":
    main()