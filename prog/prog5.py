import matplotlib.pylab as plt
import matplotlib
import numpy as np
import time as time
from prog4 import remplissage

start_time=time.time()

L=20.
R=0.4
MAX_TRIES=10000
N_MAX=int(L**2/(np.pi*R**2))
n=0 #Nombre de cercles ajoutés
x=np.empty(N_MAX) #Coordonnées du cercle
y=np.empty(N_MAX)
T=np.array([0,1,2,5,10])

x,y,n=remplissage(L,R,MAX_TRIES,T[0])
circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]
c=matplotlib.collections.PatchCollection(circles)

plt.subplot(2,3,1)
plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title(str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str("{:.2f}".format((n*np.pi*R**2/L**2)*100))+"%"
          +"\n"+"T=0")

x,y,n=remplissage(L,R,MAX_TRIES,T[1])
circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]
c=matplotlib.collections.PatchCollection(circles)

plt.subplot(2,3,2)
plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title(str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str("{:.2f}".format((n*np.pi*R**2/L**2)*100))+"%"
          +"\n"+"T=1")


x,y,n=remplissage(L,R,MAX_TRIES,T[2])
circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]
c=matplotlib.collections.PatchCollection(circles)

plt.subplot(2,3,3)
plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title(str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str("{:.2f}".format((n*np.pi*R**2/L**2)*100))+"%"
          +"\n"+"T=2")

x,y,n=remplissage(L,R,MAX_TRIES,T[3])
circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]
c=matplotlib.collections.PatchCollection(circles)

plt.subplot(2,3,4)
plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title(str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str("{:.2f}".format((n*np.pi*R**2/L**2)*100))+"%"
          +"\n"+"T=5")

x,y,n=remplissage(L,R,MAX_TRIES,T[4])
circles=[plt.Circle((xi,yi),radius=R,linewidth=0,color="b") for xi,yi in zip(x,y)]
c=matplotlib.collections.PatchCollection(circles)

plt.subplot(2,3,5)
plt.scatter(x,y,s=1)
plt.axis("scaled")
plt.xlim(0,L)
plt.ylim(0,L)
plt.gca().add_collection(c)
plt.title(str(n)+" particules de gaz"
          +"\n"+"Surface remplie: "+str("{:.2f}".format((n*np.pi*R**2/L**2)*100))+"%"
          +"\n"+"T=10")

plt.tight_layout()
plt.subplots_adjust(wspace=1)
plt.savefig("graph07.pdf",bbox_inches="tight")
plt.show()

ex_time=time.time()-start_time
print("Execution time: "+str("{:.2f}".format(ex_time))+"s")
