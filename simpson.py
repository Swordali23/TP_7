#simpson fonction approximation à partir des points d'interpolation (xi) et des valeurs de la fonction yi=f(xi)
#simpson(xi,yi) renvoie la valeur approchée de l'intégrale de f sur l'intervalle [a,b]
def simpson(f,a,b,n):
    h=(b-a)/n
    xi=[a+i*h for i in range(n+1)]
    yi=[f(x) for x in xi]
    s=0
    for i in range(0,n,2):
        s=s+yi[i]+4*yi[i+1]+yi[i+2]
    return s*h/3

#tester la méthode de Simpson sur f(x)=sin(x) sur [0,pi]
from math import pi,sin
x=simpson(sin,0,pi,1000)
print(x)