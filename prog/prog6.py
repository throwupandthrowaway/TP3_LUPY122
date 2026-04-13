import numpy as np
from prog4 import remplissage
import matplotlib.pyplot as plt
import time as time

start_time=time.time()

L=20.
R=0.4
MAX_TRIES=10000
N_MAX=int(L**2/(np.pi*R**2))
n=0
M=100
T=np.arange(0,10.5,0.5)
k=np.pi*R**2/(L**2) #Facteur d'échelle
mean_S=np.empty(M)
sd_S=np.empty(M)

for j in range(len(T)):
    resultats=np.empty(M)
    for i in range(M):
        _,_,n=remplissage(L,R,MAX_TRIES,T[j])
        resultats[i]=n
    mean_S[j]=np.mean(resultats)*k
    sd_S[j]=np.std(resultats)*k

plt.plot(T,mean_S,'o-')
plt.xlabel('T')
plt.ylabel('Portion de surface moyenne')
plt.title('Portion de surface adsorbée en fonction de T')
plt.savefig("graph08.pdf",bbox_inches="tight")
plt.show()

ex_time=time.time()-start_time
print("Execution time: "+str("{:.2f}".format(ex_time))+"s")