CC = gcc

all: merge_sort quick_sort

merge_sort: mergeSort.c
	@ $(CC) mergeSort.c -o mergeSort

quick_sort: quickSort.c
	@ $(CC) quickSort.c -o quickSort