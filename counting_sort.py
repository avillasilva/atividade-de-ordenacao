from math import fabs

def find_max(input):
    """
    Funcao auxiliar para encontrar o maior valor de uma lista.

    Parametros
    ----------
    input : array
        A lista de numeros para se procurar.
    
    Retorna
    -------
    max : max value
        O maior valor da lista.
    """
    max = 0
    for i in input:
        if i > max:
            max = i  
    return max

def find_min(input):
    """
    Funcao auxiliar para encontrar o menor valor de uma lista.

    Parametros
    ----------
    input : array
        A lista de numeros para se procurar.
    
    Retorna
    -------
    min: min value
        O menor valor da lista.
    """
    min = 0
    for i in input:
        if i < min:
            min = i
    return min

def counting_sort(input):
    """
    Counting sort para valores reais.

    Parametros
    ----------
    input : array
        Array contendo os valores a serem ordenados.

    Retorna
    -------
    input : array
        Array com os valores ordenados.    
    """

    # O valor maximo e o valor minimo sao necessarios para que o algoritmo
    # funcione para entrada possua numeros negativos.
    min = int(fabs(find_min(input))) + 1
    max = int(find_max(input)) + min

    # Inicializa o vetor auxiliar e o vetor de saida com zeros.
    # O vetor aux precisa ter max + 1 elementos devido aos deslocamentos na linha 29
    # e as somas na linha 34.
    # Ex: max = 19, min = 0 -> aux[max + min] -> aux[19 + 0] 
    aux = [min for i in range(max + 1)]
    output = [0 for i in range(len(input))] 

    # Contagem dos elementos.
    for i in input:
        aux[i + min] += 1

    # aux[i] = aux[0] + ... + aux[i]
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1] - min

    # Organiza os elementos nas posicoes ordenadas subtraindo os deslocamentos.
    for i in range(len(input)):
        output[aux[input[i] + min] - min - 1] = input[i]
        aux[input[i] + min] -= 1
    
    for i in range(0, len(input)):
        input[i] = output[i]

    return input

print("Counting Sort")

print("Input: ", end = '')

input = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]

for i in input:
    print(i, end=' ')

print()

output = counting_sort(input)

print("Output: ", end = '')

for i in output:
    print(i, end = ' ')

print()