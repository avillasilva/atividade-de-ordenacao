def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j != 0 and arr[j] < arr[j - 1]:
            aux = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = aux
            j -= 1
    return arr

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

    input = insertion_sort(input)

    for i in input:
        fout.write(str(i) + '\n')

    fin.close()
    fout.close()

ord("instancias-num/num.1000.1.in", "insertion_sort/1000-1.txt")
ord("instancias-num/num.1000.2.in", "insertion_sort/1000-2.txt")
ord("instancias-num/num.1000.3.in", "insertion_sort/1000-3.txt")
ord("instancias-num/num.1000.4.in", "insertion_sort/1000-4.txt")
ord("instancias-num/num.10000.1.in", "insertion_sort/10000-1.txt")
ord("instancias-num/num.10000.2.in", "insertion_sort/10000-2.txt")
ord("instancias-num/num.10000.3.in", "insertion_sort/10000-3.txt")
ord("instancias-num/num.10000.4.in", "insertion_sort/10000-4.txt")
ord("instancias-num/num.100000.1.in", "insertion_sort/100000-1.txt")
ord("instancias-num/num.100000.2.in", "insertion_sort/100000-2.txt")
ord("instancias-num/num.100000.3.in", "insertion_sort/100000-3.txt")
ord("instancias-num/num.100000.4.in", "insertion_sort/100000-4.txt")