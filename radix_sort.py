from math import fabs
from math import pow

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

def counting_sort(input, digit):
    """
    Counting sort modificado para ordenar os valores de uma lista
    levando consideracao o digito especificado.

    Parametros
    ----------
    input : array
        Array contendo os valores a serem ordenados.
    digit : int
        Especifica a qual digito a ordenacao deve ser feita. Ex: menos significativo = 0.

    Retorna
    -------
    output : array
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
        index = int(digit_at(i, digit))
        aux[index + min] += 1

    # aux[i] = aux[0] + ... + aux[i]
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1] - min

    # Organiza os elementos nas posicoes ordenadas subtraindo os deslocamentos.
    for i in range(len(input) - 1, -1, -1):
        index = int(digit_at(input[i], digit))
        output[aux[index + min] - min - 1] = input[i]
        aux[index + min] -= 1
    
    return output

def digit_at(number, digit):
    if number > 0:
        return (number /  (10 ** digit)) % 10
    else:
        return (number / (10 ** digit)) % -10

def radix_sort(input):
    """
    Radix sort que utiliza o counting sort como subrotina.

    Parametros
    ----------
    input : array
        Array a ser ordenado.

    Retorna
    ------
    input : array
        Array com os valores ordenados.
    """
    min = int(fabs(find_min(input)))
    max = int(fabs(find_max(input))) + min
    
    digit = 0
    while max > 0:
        input = counting_sort(input, digit) 
        max = int(max / 10)
        digit += 1
    
    return input

input = [329, 457, 657, 839, 436, 720, 355]

print("Input: ", end=' ')
for i in input:
    print(i, end = ' ')

print()

input = radix_sort(input)

print("Output: ", end=' ')
for i in input:
    print(i, end = ' ')
print()