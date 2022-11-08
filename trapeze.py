#trapeze fonction approximation à partir des points d'interpolation (xi) et des valeurs de la fonction yi=f(xi)
#trapeze(xi,yi) renvoie la valeur approchée de l'intégrale de f sur l'intervalle [a,b]
from math import pi,sin

def trapeze(f,a,b,n):
    print("ok")
    h=(b-a)/n
    xi=[a+i*h for i in range(n+1)]
    yi=[f(x) for x in xi]
    s=0
    for i in range(n):
        s=s+(yi[i]+yi[i+1])/2
    return s*h


x=trapeze(sin,0,pi,1000)
print(x)