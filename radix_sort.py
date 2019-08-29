from math import fabs
from math import pow

def digit_at(number, digit):
    if number > 0:
        return (number /  (10 ** digit)) % 10
    else:
        return (number / (10 ** digit)) % -10

def find_max(input):
    max = 0
    for i in input:
        if i > max:
            max = i  
    return max

def find_min(input):
    min = 0
    for i in input:
        if i < min:
            min = i
    return min

def find_maxd(input, digit):
    max = digit_at(input[0], digit)
    for i in input:
        if digit_at(i, digit) > max:
            max = digit_at(i, digit)  
    return max

def find_mind(input, digit):
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
    min = int(fabs(find_mind(input, digit))) + 1
    max = int(find_maxd(input, digit)) + min

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

# input = [-10, 0, 1000, 8, 5, -20]
# input = radix_sort(input)

# for i in input:
#     print(i)

ord("instancias-num/num.1000.1.in", "radix_sort/1000-1.txt")
ord("instancias-num/num.1000.2.in", "radix_sort/1000-2.txt")
ord("instancias-num/num.1000.3.in", "radix_sort/1000-3.txt")
ord("instancias-num/num.1000.4.in", "radix_sort/1000-4.txt")
ord("instancias-num/num.10000.1.in", "radix_sort/10000-1.txt")
ord("instancias-num/num.10000.2.in", "radix_sort/10000-2.txt")
ord("instancias-num/num.10000.3.in", "radix_sort/10000-3.txt")
ord("instancias-num/num.10000.4.in", "radix_sort/10000-4.txt")
ord("instancias-num/num.100000.1.in", "radix_sort/100000-1.txt")
ord("instancias-num/num.100000.2.in", "radix_sort/100000-2.txt")
ord("instancias-num/num.100000.3.in", "radix_sort/100000-3.txt")
ord("instancias-num/num.100000.4.in", "radix_sort/100000-4.txt")