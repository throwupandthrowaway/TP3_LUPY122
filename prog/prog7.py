import numpy as np
import matplotlib.pyplot as plt
from prog1 import remplissage

L=20.
R=0.4
M=20
k=np.pi*R**2/L**2

max_tries_list=[1000,2000,4000,8000,16000,32000]
mean_S=np.empty(len(max_tries_list))
sd_S=np.empty(len(max_tries_list))

for j,MAX_TRIES in enumerate(max_tries_list):
    resultats=np.empty(M)
    for i in range(M):
        _,_,n=remplissage(L,R,MAX_TRIES)
        resultats[i]=n
    mean_S[j]=np.mean(resultats)*k
    sd_S[j]=np.std(resultats)*k

plt.errorbar(max_tries_list,mean_S,yerr=sd_S,fmt='o-')
plt.xscale('log')
plt.xlabel('MAX_TRIES')
plt.ylabel('Portion de surface moyenne')
plt.show()