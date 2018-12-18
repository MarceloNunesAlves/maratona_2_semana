import numpy as np

array_test = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print()

print(np.array([[ True, True, True],
[ True, True, True],
[ True, True, True]]))

array_saida = []
for val in array_test:
    if(val%2!=0):
        array_saida.append(val)

print(array_saida)

array_saida = []
for val in array_test:
    if(val%2!=0):
        array_saida.append(-1)
    else:
        array_saida.append(val)

print(array_saida)

array_1d = np.arange(10)
array_2d = np.split(array_1d, 2)
print(array_2d)

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(np.concatenate((a, b),axis=0))

a = np.concatenate(a, axis=None)
b = np.concatenate(b, axis=None)

a = np.array([1,2,3])

