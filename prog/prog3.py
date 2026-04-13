import numpy as np
from prog1 import remplissage

L=20.
R=0.4
MAX_TRIES=1000
N_MAX=int(L**2/(np.pi*R**2))
n=0
M=20
resultats=np.empty(M)

for i in range(M):
    _,_,n=remplissage(L,R,MAX_TRIES)
    resultats[i]=n

mean=np.mean(resultats)
sd=np.std(resultats)
k=np.pi*R**2/(L**2) #Facteur d'échelle

mean_S=k*mean   #Moyenne de la fraction de surface
sd_S=k*sd   #Ecart-type de la fraction de surface
print("Moyenne de la fraction de surface avec particules adsorbées: "+str(mean_S*100)+"%")
print("Ecart-type de la fraction de surface avec particules adsorbées: "+str(sd_S*100)+"%")
