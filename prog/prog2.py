import matplotlib.pylab as plt
import matplotlib
import numpy as np
from prog1 import remplissage

L=20.
R=0.4
MAX_TRIES=1000
N_MAX=int(L**2/(np.pi*R**2))
n=0 #Nombre de cercles ajoutés
x=np.empty(N_MAX) #Coordonnées du cercle
y=np.empty(N_MAX)

x,y,n=remplissage(L,R,MAX_TRIES)

circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]

c=matplotlib.collections.PatchCollection(circles)

plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title("Surface cristalline de 20x20 unités remplie de "+str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str((n*np.pi*R**2/L**2)*100)+"%")
plt.savefig("graph02.pdf",bbox_inches="tight")
plt.show()