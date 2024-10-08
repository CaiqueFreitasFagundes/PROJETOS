import numpy as np
# numpy é uma biblioteca de álgebra linear para Python, a razão pela qual é tão importante para a ciência de dados com Python é que quase todas as bibliotecas dependem do NumPy como um dos principais blocos de construção. Ela é principalmente usada para realizar cálculos em arrays multidimensionais e matrizes.

# ## Criando Arrays = np.array()
#  para criar uma array, voce pode passar uma lista, e depois converter para um array numpy usando np.array(lista).

lista = [1, 2, 3, 4, 5]
lista_convertida = np.array(lista)
print(lista_convertida)
# R: array([1 2 3 4 5])

# Ao passar uma lista de listas, voce cria uma matriz multidimensional.

lista2 = [[1,2,3], [4,5,6], [7,8,9]]
lista2_convertida = np.array(lista2)
print(lista2_convertida)
# R:[[1 2 3] 
#  [4 5 6] 
#  [7 8 9]]

# ## Gerando uma Array = np.arange()
# O arange é uma função que retorna valores uniformemente espaçados dentro de um determinado intervalo.
np.arange(0, 10)
# R: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(0, 10, 2)
# R: array([0, 2, 4, 6, 8])

# ## Arrays de zeros e uns = np.zeros() e np.ones()
#  Essas funções criam arrays de zeros ou uns.
np.zeros(3)
# R: array([0., 0., 0.])
np.zeros((5,5))
# R: array([[0., 0., 0., 0., 0.],
#            [0., 0., 0., 0., 0.],
#            [0., 0., 0., 0., 0.],
#            [0., 0., 0., 0., 0.],
#            [0., 0., 0., 0., 0.]])
np.ones(2)
# R: array([1., 1.])
np.ones((3,3))
# R: array([[1., 1., 1.],
#            [1., 1., 1.],
#            [1., 1., 1.]])
np.eye(4)
# Cria uma matriz identidade de 4x4
# R: array([[1., 0., 0., 0.],
#           [0., 1., 0., 0.],
#           [0., 0., 1., 0.],
#           [0., 0., 0., 1.]])

#  ## Linspace
# O linspace é um método especial que retorna um número de valores uniformemente espaçados entre dois números.
np.linspace(0, 10, 3)
# R: array([ 0.,  5., 10.])
np.linspace(0, 10, 50)
print(np.linspace(0, 10, 50))

#  ## Random
# Numpy também tem muitas maneiras de criar arrays de números aleatórios:
np.random.rand(2)
# R: array([0.42829726, 0.99657423])
# Podemos aplicar matrizes no np.random.rand()
np.random.rand(5,5)
print(np.random.rand(5,5))
#  np.random.randn() retorna uma amostra (ou amostras) da distribuição "normal". Diferente de rand que é uniforme:
np.random.randn(2)
# R: array([0.3990465 , 0.29178658])
# Qual a principal diferença entre rand e randn?
# R: rand() gera números aleatórios entre 0 e 1 com chances iguais. Já randn() gera números em torno de 0, com a maioria concentrada perto de 0 e alguns mais distantes, como uma montanha com o topo no zero.

# podemos usar np.random.randint() para retornar inteiros aleatórios de um intervalo baixo para alto.

#  ## reshape()
# Retorna um array contendo os mesmos dados com uma nova forma.
arr = np.arange(25)
print(arr)

arr = arr.reshape(5,5)
print(arr)

# ## max, min, argmax, argmin
# Esses são métodos úteis para encontrar valores máximos ou mínimos. Ou para encontrar seus índices de onde eles ocorrem no array.
arr = np.random.randint(0,50,10)
print(arr)
print(arr.max())
print(arr.min())
print(arr.argmax())
print(arr.argmin())
