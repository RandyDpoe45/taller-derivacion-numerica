# coding: utf-8
# Your code here!
from sympy import *
import numpy as np
from scipy.misc import derivative
def der2(x1,h):
    x=Symbol('x')
    f=x*(np.e**x)
    res=N(f.subs({x:x1+h}))
    res2=N(f.subs({x:x1}))
    return ((res-res2)/h)
def der3(x1,h):
    x=Symbol('x')
    f=x*(np.e**x)
    res=N(3*f.subs({x:x1})/(2*h))
    res1=N(-4*f.subs({x:x1-h})/(2*h))
    res2=N(f.subs({x:x1-(2*h)})/(2*h))
    return (res1+res2+res)

def elviejorichi(x1,h):
    a=[]
    x=Symbol('x')
    f=x*(np.e**x)
    i=-2*h
    while(i<3*h):
        a.append(f.subs({x:x1+i}))
        i+=h
    ini=(a[4]-a[0])/(4*h)
    fin=(a[3]-a[1])/(2*h)
    return ((4*ini/3)-(fin/3))
    
def main():
    x=Symbol('x')
    f=diff(x*(np.e**x),x)
    e=f.subs({x:1})
    for i in range(1,17):
        r=der2(1,1/(10**i))
        r2=der3(1,1/(10**i))
        r3=elviejorichi(1,1/(10**i))
        print("|"+str(e) +"| "+str(1/(10**i))+" | "+str(r) +"|"+ str(abs(r-e))+"|" +str(r2)+"|"+str(abs(r2-e))+"|"+str(r3)+"|"+str(abs(r3-e))+"|")
        
    
    
if __name__ == "__main__":
    main()
