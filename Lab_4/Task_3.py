import numpy as np
import sympy as syp
from sympy import Function, dsolve, Derivative
from sympy.abc import x
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math

def diffur(_, y):
	return -2 * y

y = Function('y')  # создание символьной функции y
ageneral = dsolve(Derivative(y(x), x) + 2 * y(x), y(x), ics={y(0): syp.sqrt(2)})
# решение символьного дифференциального уравнения
print('analytic solution:')
print(ageneral)

ngeneral = syp.lambdify(x, ageneral.rhs)
# преобразование общего решения дифференциального уравнения в функцию, которую можно вычислить численно

numeric = solve_ivp(diffur, [0, 10], [math.sqrt(2)], t_eval=np.linspace(0, 10, num=1000))
# решение численного дифференциального уравнения
# интервал интегрирования [0, 10], начальное значение [math.sqrt(2)]
# значения времени t_eval, которые получаются с использованием функции linspace из модуля numpy

fig, ax = plt.subplots()

plt.minorticks_on()
plt.grid(True, "major", "both", color="#888888")
plt.grid(True, "minor", "both", linestyle='--')

# построение графика численного решения и аналитического решения
x = np.linspace(0, 10, num=1000)

ax.plot(numeric.t, numeric.y[0], label='numeric', color="#00FF00")
ax.plot(x, ngeneral(x), label='analytic', color="#1E90FF", linestyle='--')

plt.legend()
plt.title('Numeric and Analytic solution for y(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('Решения.png')
plt.show()



fig, ax = plt.subplots()

ax.plot(x, ngeneral(x)-numeric.y[0], color="#4B0082")

plt.minorticks_on()
plt.grid(True, "major", "both", color="#888888")
plt.grid(True, "minor", "both", linestyle='--')

plt.title('Difference')
plt.xlabel('x')
plt.ylabel('yA - yN')

plt.savefig('Разность решений.png')
plt.show()
