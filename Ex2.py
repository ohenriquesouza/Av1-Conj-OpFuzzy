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

# domínio (universo de discurso) e particionando em 4 funções de pertinência
dominio = [i * 0.1 for i in range(100)]  # intervalo de 0 a 10 com passo de 0.1
a, b, c, d = 0, 3.33, 6.66, 10  # divisões do domínio

# Amostras para fuzzificação
amostra1 = 2
amostra2 = 7

# Calculando a fuzzificação para cada amostra em cada função
triangular1_values = [pertinencia_triangular(amostra1, 0, 3.33, 6.66),
                      pertinencia_triangular(amostra1, 3.33, 6.66, 10)]
triangular2_values = [pertinencia_triangular(amostra2, 0, 3.33, 6.66),
                      pertinencia_triangular(amostra2, 3.33, 6.66, 10)]

# Plotando o universo de discurso e os graus de ativação das amostras
plt.plot(dominio, [pertinencia_triangular(x, 0, 3.33, 6.66) for x in dominio], label="Triangular 1")
plt.plot(dominio, [pertinencia_triangular(x, 3.33, 6.66, 10) for x in dominio], label="Triangular 2")

# Destacando as amostras
plt.scatter([amostra1, amostra2], triangular1_values, color="red", label="Amostra 1")
plt.scatter([amostra1, amostra2], triangular2_values, color="blue", label="Amostra 2")

plt.title("Análise Gráfica das Funções de Pertinência e Fuzzificação das Amostras")
plt.xlabel("Universo de Discurso (x)")
plt.ylabel("Pertinência")
plt.legend()
plt.grid(True)
plt.show()

# Análise textual comparativa
print("Análise Textual:")
print(f"Amostra 1 (x = {amostra1}):")
print(f"  - Grau de ativação na função Triangular 1: {triangular1_values[0]}")
print(f"  - Grau de ativação na função Triangular 2: {triangular1_values[1]}")
print(f"Amostra 2 (x = {amostra2}):")
print(f"  - Grau de ativação na função Triangular 1: {triangular2_values[0]}")
print(f"  - Grau de ativação na função Triangular 2: {triangular2_values[1]}")