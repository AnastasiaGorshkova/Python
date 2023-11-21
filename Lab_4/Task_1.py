from sympy import Matrix
from sympy.abc import lamda, mu, rho
from sympy import pprint

A = Matrix([[0, 0, 0, -1/rho, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, -1/rho, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1/rho, 0, 0, 0],
            [-(lamda+2*mu),  0, 0, 0, 0, 0, 0, 0, 0],
            [0, -mu, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -mu, 0, 0, 0, 0, 0, 0],
            [-lamda, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-lamda, 0, 0, 0, 0, 0, 0, 0, 0]
		    ])

pprint(A)
print('Собственные значения в символьном виде:')
for data in list(A.eigenvals().items()):
    print(data)
