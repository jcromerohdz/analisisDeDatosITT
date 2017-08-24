import numpy as np
import scipy as sc
import matplotlib as plot
array_zeros = np.zeros(10)  # vector en ceros
array_unos = np.ones(10)    # vectores asignados en unos
lista = [0,2,4,5, 2.3,5.7,0,0,0,4.4,3.3]
#np.nonzero   regresa solo los indices donde no hay zeros.
lista_random  = np.arange(1, 100)# inicializa vectores consecutivos
  #matrices
matriz = np.arange(12).reshape(3,4)
#matriz cuadrada con identidad unos en la diagonal

matriz_cuadrada = np.eye (10)

#matrices dimencionales
matriz_bi = np.random.random(10)
matriz_bi2 = np.random.random((4,3)) #random con matrices

# para minimo o maximo seria matriz_bi2.min()
#  numpy.diag(matriz_bi2)
# matriz - min  /   max-min    normalizacion de datos
#  .dot   multiplicacion de matrices




