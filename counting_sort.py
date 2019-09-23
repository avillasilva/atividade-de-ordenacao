from math import fabs
import sys

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
    min = find_min(input)
    max = find_max(input)
    limit = max - min + 1

    # Inicializa o vetor auxiliar e o vetor de saida com zeros.
    aux = [0 for i in range(limit)]
    output = [0 for i in range(len(input))] 

    # Contagem dos elementos.
    for i in input:
        aux[i - min] += 1

    # aux[i] = aux[0] + ... + aux[i]
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]

    # Organiza os elementos nas posicoes ordenadas subtraindo os deslocamentos.
    for i in range(len(input)):
        output[aux[input[i] - min] - 1] = input[i]
        aux[input[i] - min] -= 1
    
    for i in range(0, len(input)):
        input[i] = output[i]

    return input

def ord(file_in, file_out):
    """
    Funcao auxiliar para ordenar os casos de testes.
    """
    fin = open(file_in, 'r')
    fout = open(file_out, 'w')
    input = []
    lines = fin.readlines()
    
    for line in lines:
        input.append(int(line))

    input = counting_sort(input)

    for i in input:
        fout.write(str(i) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    ord(sys.argv[1], sys.argv[2])

# ord("instancias-num/num.1000.1.in", "counting_sort/1000-1.txt")
# ord("instancias-num/num.1000.2.in", "counting_sort/1000-2.txt")
# ord("instancias-num/num.1000.3.in", "counting_sort/1000-3.txt")
# ord("instancias-num/num.1000.4.in", "counting_sort/1000-4.txt")
# ord("instancias-num/num.10000.1.in", "counting_sort/10000-1.txt")
# ord("instancias-num/num.10000.2.in", "counting_sort/10000-2.txt")
# ord("instancias-num/num.10000.3.in", "counting_sort/10000-3.txt")
# ord("instancias-num/num.10000.4.in", "counting_sort/10000-4.txt")
# ord("instancias-num/num.100000.1.in", "counting_sort/100000-1.txt")
# ord("instancias-num/num.100000.2.in", "counting_sort/100000-2.txt")
# ord("instancias-num/num.100000.3.in", "counting_sort/100000-3.txt")
# ord("instancias-num/num.100000.4.in", "counting_sort/100000-4.txt")