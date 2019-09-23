from math import fabs
from math import pow
import sys

def digit_at(number, position):
    """
    Funcao auxiliar que retorna um digito de um numero na posicao especificada
    levando em consideracao o sinal do numero.

    Paramentros
    -----------
    number : int
        Numero de onde retirar o digito.
    position: int
        Posicao do digito. Ex: menos significativo = 0.
    
    Retorna
    -------
    Digito na posicao especificada.
    """
    if number > 0:
        return (number /  (10 ** position)) % 10
    else:
        return (number / (10 ** position)) % -10

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

def find_max_digit(input, digit):
    """
    Uma funcao para encontrar o maior digito na posicao especificada
    dentre todos os elementos de um array.

    Parametros
    ----------
    input : array
        Array contendo os valores.
    digit: int
        Digito a ser considerado. Ex: menos significativo = 0.

    Retorna
    -------
        O maior digito encontrado na posicao fornecida entre todos os
        elementos do array.
    """
    max = digit_at(input[0], digit)
    for i in input:
        if digit_at(i, digit) > max:
            max = digit_at(i, digit)  
    return max

def find_min_digit(input, digit):
    """
    Uma funcao para encontrar o menor digito na posicao especificada
    dentre todos os elementos de um array.

    Parametros
    ----------
    input : array
        Array contendo os valores.
    digit: int
        Digito a ser considerado. Ex: menos significativo = 0.

    Retorna
    -------
        O menor digito encontrado na posicao fornecida entre todos os
        elementos do array.
    """
    min = digit_at(input[0], digit)
    for i in input:
        if digit_at(i, digit) < min:
            min = digit_at(i, digit)  
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
    min = int(find_min_digit(input, digit))
    max = int(find_max_digit(input, digit))
    limit = max - min + 1

    aux = [0 for i in range(limit)]
    output = [0 for i in range(len(input))] 

    # Contagem dos elementos.
    for i in input:
        index = int(digit_at(i, digit))
        aux[index - min] += 1

    # aux[i] = aux[0] + ... + aux[i]
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]

    # Organiza os elementos nas posicoes ordenadas subtraindo os deslocamentos.
    for i in range(len(input) - 1, -1, -1):
        index = int(digit_at(input[i], digit))
        output[aux[index - min] - 1] = input[i]
        aux[index - min] -= 1
    
    return output

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

    input = radix_sort(input)

    for i in input:
        fout.write(str(i) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    ord(sys.argv[1], sys.argv[2])

# ord("instancias-num/num.1000.1.in", "radix_sort/1000-1.txt")
# ord("instancias-num/num.1000.2.in", "radix_sort/1000-2.txt")
# ord("instancias-num/num.1000.3.in", "radix_sort/1000-3.txt")
# ord("instancias-num/num.1000.4.in", "radix_sort/1000-4.txt")
# ord("instancias-num/num.10000.1.in", "radix_sort/10000-1.txt")
# ord("instancias-num/num.10000.2.in", "radix_sort/10000-2.txt")
# ord("instancias-num/num.10000.3.in", "radix_sort/10000-3.txt")
# ord("instancias-num/num.10000.4.in", "radix_sort/10000-4.txt")
# ord("instancias-num/num.100000.1.in", "radix_sort/100000-1.txt")
# ord("instancias-num/num.100000.2.in", "radix_sort/100000-2.txt")
# ord("instancias-num/num.100000.3.in", "radix_sort/100000-3.txt")
# ord("instancias-num/num.100000.4.in", "radix_sort/100000-4.txt")