import math
import matplotlib.pyplot as plt

# Funções de pertinência

# Triangular
def pertinencia_triangular(x, a, b, c):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0.0

# Trapezoidal
def pertinencia_trapezoidal(x, a, b, c, d):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0.0

# Gaussiana
def pertinencia_gaussiana(x, m, sigma):
    return math.exp(-0.5 * ((x - m) / sigma) ** 2)

# Sigmoidal
def pertinencia_sigmoidal(x, a, c):
    return 1 / (1 + math.exp(-a * (x - c)))

# Sino
def pertinencia_sino(x, a, b, c):
    return 1 / (1 + abs((x - c) / a) ** (2 * b))

# S
def pertinencia_s(x, a, b):
    if x <= a:
        return 0.0
    elif a < x <= (a + b) / 2:
        return 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x <= b:
        return 1 - 2 * ((x - b) / (b - a)) ** 2
    else:
        return 1.0

# Z
def pertinencia_z(x, a, b):
    if x <= a:
        return 1.0
    elif a < x <= (a + b) / 2:
        return 1 - 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x <= b:
        return 2 * ((x - b) / (b - a)) ** 2
    else:
        return 0.0

# Cauchy
def pertinencia_cauchy(x, x0, gamma):
    return 1 / (1 + ((x - x0) / gamma) ** 2)

# Gaussiana Dupla
def pertinencia_gaussiana_dupla(x, m1, sigma1, m2, sigma2):
    if x <= (m1 + m2) / 2:
        return math.exp(-0.5 * ((x - m1) / sigma1) ** 2)
    else:
        return math.exp(-0.5 * ((x - m2) / sigma2) ** 2)

# User Defined 1 (Quadrática)
def user_defined_1(x, c, l):
    if abs(x - c) <= l:
        return 1 - ((x - c) / l) ** 2
    else:
        return 0.0

# User Defined 2 (Exponencial)
def user_defined_2(x, b, d):
    return math.exp(-b * abs(x - d))

# Definindo o intervalo de x manualmente
x_values = [i * 0.1 for i in range(100)]  # de 0 a 10 com passo de 0.1

# Plot da função Triangular
a, b, c = 2, 5, 8
triangular_values = [pertinencia_triangular(x, a, b, c) for x in x_values]
plt.plot(x_values, triangular_values, label="Triangular")
plt.title("Função de Pertinência Triangular")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Trapezoidal
a, b, c, d = 1, 3, 7, 9
trapezoidal_values = [pertinencia_trapezoidal(x, a, b, c, d) for x in x_values]
plt.plot(x_values, trapezoidal_values, label="Trapezoidal")
plt.title("Função de Pertinência Trapezoidal")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Gaussiana
m, sigma = 5, 1.5
gaussiana_values = [pertinencia_gaussiana(x, m, sigma) for x in x_values]
plt.plot(x_values, gaussiana_values, label="Gaussiana")
plt.title("Função de Pertinência Gaussiana")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Sigmoidal
a, c = 1, 5
sigmoidal_values = [pertinencia_sigmoidal(x, a, c) for x in x_values]
plt.plot(x_values, sigmoidal_values, label="Sigmoidal")
plt.title("Função de Pertinência Sigmoidal")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Sino
a, b, c = 2, 3, 5
sino_values = [pertinencia_sino(x, a, b, c) for x in x_values]
plt.plot(x_values, sino_values, label="Sino")
plt.title("Função de Pertinência Sino")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função S
a, b = 3, 6
s_values = [pertinencia_s(x, a, b) for x in x_values]
plt.plot(x_values, s_values, label="S")
plt.title("Função de Pertinência S")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Z
a, b = 3, 6
z_values = [pertinencia_z(x, a, b) for x in x_values]
plt.plot(x_values, z_values, label="Z")
plt.title("Função de Pertinência Z")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Cauchy
x0, gamma = 5, 1
cauchy_values = [pertinencia_cauchy(x, x0, gamma) for x in x_values]
plt.plot(x_values, cauchy_values, label="Cauchy")
plt.title("Função de Pertinência Cauchy")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função Gaussiana Dupla
m1, sigma1, m2, sigma2 = 4, 1, 6, 1.5
gaussiana_dupla_values = [pertinencia_gaussiana_dupla(x, m1, sigma1, m2, sigma2) for x in x_values]
plt.plot(x_values, gaussiana_dupla_values, label="Gaussiana Dupla")
plt.title("Função de Pertinência Gaussiana Dupla")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função User Defined 1 (Quadrática)
c, l = 5, 2
user_defined_1_values = [user_defined_1(x, c, l) for x in x_values]
plt.plot(x_values, user_defined_1_values, label="User Defined 1 (Quadrática)")
plt.title("Função de Pertinência User Defined 1 (Quadrática)")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Plot da função User Defined 2 (Exponencial)
b, d = 0.5, 5
user_defined_2_values = [user_defined_2(x, b, d) for x in x_values]
plt.plot(x_values, user_defined_2_values, label="User Defined 2 (Exponencial)")
plt.title("Função de Pertinência User Defined 2 (Exponencial)")
plt.xlabel("x")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()
