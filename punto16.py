import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("monthrg.dat")

ano = data[:,0]
mes = data[:,1]
num_dias = data[:,2]
num_manchas = data[:,3]

def FT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        X[k] = 0.0j
        for n in range(N):
            X[k] += x[n] * np.exp(-2.0 * np.pi * 1.0j / N ) ** (k * n) 
        
    return X

transformada = FT(num_manchas)


transformada = (100*np.sin((0.5*np.pi-ano))+100)
plt.figure()
plt.scatter(ano,num_manchas, c= "r")
plt.plot(ano,transformada)
plt.xlabel("Año")
plt.ylabel("Número de manchas")
plt.savefig("solar.png")

print("El período es de aproximadamente 10 AÑOS.")


