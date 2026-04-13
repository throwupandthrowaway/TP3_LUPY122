import numpy as np
import numba
from numba import njit

L=20.
R=0.4
MAX_TRIES=1000
N_MAX=int(L**2/(np.pi*R**2))
n=0 #Nombre de cercles ajoutés
x=np.empty(N_MAX) #Coordonnées du cercle
y=np.empty(N_MAX)

@njit
def coord(L,R): #Coordonnée aléatoire entre R et L-R (Limites du carré pour le centre du cercle)
    return R+np.random.rand()*(L-2*R)

@njit
def place_libre(n,x,y,x_new,y_new):
    if n==0:
        return 1
    else:
        for i in range(n): #On calcule la distance entre le centre de la i-ème particule et la nouvelle
            dx=abs(x_new-x[i])
            dy=abs(y_new-y[i])
            r=np.sqrt(dx**2+dy**2)
            if r<2*R:
                return 0
                break
        return 1

@njit
def remplissage(L,R,MAX_TRIES):
    x=np.empty(N_MAX)
    y=np.empty(N_MAX)
    n=0
    echecs=0
    while echecs<MAX_TRIES:
        x_new=coord(L,R)
        y_new=coord(L,R)
        libre=place_libre(n,x,y,x_new,y_new)
        if libre==1:
            x[n]=x_new
            y[n]=y_new
            n+=1
            echecs=0
            
        else:
            echecs+=1
    return x[:n],y[:n],n

x,y,n=remplissage(L,R,MAX_TRIES)
for i in range(n):
    print(x[i],"",y[i])
print("Particules adsorbées: "+str(n))
frac=(n*np.pi*R**2/L**2)*100
print("Portion de surface avec adsorption: "+str(frac)+"%")
