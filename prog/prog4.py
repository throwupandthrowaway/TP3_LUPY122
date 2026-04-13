import numpy as np
from prog1 import coord, place_libre

L=20.
R=0.4
MAX_TRIES=10000
r_surf=0.05
U=10.0

def dist_latt(x_new,y_new):
    x_near=np.rint(x_new)   #Atome le plus proche = arrondi à l'entier le plus proche
    y_near=np.rint(y_new)
    return np.sqrt((x_new-x_near)**2+(y_new-y_near)**2)

def remplissage(L,R,MAX_TRIES,T):
    N_MAX=int(L**2/(np.pi*R**2))
    x=np.empty(N_MAX)
    y=np.empty(N_MAX)
    n=0
    echecs=0
    while echecs<MAX_TRIES:
        x_new=coord(L,R)
        y_new=coord(L,R)
        if place_libre(n,x,y,x_new,y_new)==1:
            d=dist_latt(x_new,y_new)
            if d<r_surf or T*np.log(np.random.rand())<-U:   #Aspect probabiliste
                x[n]=x_new
                y[n]=y_new
                n+=1
                echecs=0
            else:
                echecs+=1
        else:
            echecs+=1
    return x[:n],y[:n],n

x,y,n= remplissage(L,R,MAX_TRIES,T=0)
k=np.pi*R**2/(L**2)
print(str(n)+" particules adsorbées, "+str(k*n*100)+"% de la surface remplie")