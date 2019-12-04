import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("valores.txt")


def prob(x,sigma):
    y = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x**2)/(sigma**2)))
    return y

def probtotal(xprobs_k):
    probtotal = 1
    for i in range(len(xprobs_k)):
        probtotal = probtotal * xprobs_k[i]
    return probtotal

probs_k = prob(data,1)
probtotal = probtotal(probs_k)
print(probtotal)
        
	
	
sigma_delta = 1.0
N = 100000
lista = [probtotal]

for i in range(1,N):
    propuesta  = lista[i-1] + sigma_delta * (np.random.random()-0.5)
    r = min(1,prob(propuesta,1)/prob(lista[i-1],1))
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])
        
		
plt.hist(np.array(lista), density = True)
plt.savefig("sigma.png")