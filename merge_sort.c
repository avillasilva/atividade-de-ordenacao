#include <stdio.h>

/**
 * A utilitarian function to print the elements of an array.
 * */
void printArray(int arr[], int n)
{
    int i;
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);
    
    printf("\n");
}

/**
 * The merge function to merge the halves.
 * */
void merge(int arr[], int left, int middle, int right)
{
    int i, j, k;
    int nl = middle - left + 1;
    int nr = right - middle;

    int l[nl];
    int r[nr];

    for (i = 0, j = left; j < middle + 1; i++, j++)
        l[i] = arr[j];

    for (i = 0, j = middle + 1; j <= right; i++, j++)
        r[i] = arr[j];

    for (i = 0, j = 0, k = left; i < nl && j < nr; k++)
    {
        if (l[i] <= r[j])
        {
            arr[k] = l[i];
            i++;
        }

        else
        {
            arr[k] = r[j];
            j++;
        }
    }

    while (i < nl)
    {
        arr[k] = l[i];
        i++;
        k++;
    }

    while (j < nr)
    {
        arr[k] = r[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right)
{
    if (right > left)
    {
        int middle = (right + left) / 2;
        mergeSort(arr, left, middle);
        mergeSort(arr, middle + 1, right);
        merge(arr, left, middle, right);
    }
}

int main()
{
    int i, j, k, arr[] = {12, 11, 13, 5, 6, 7};

    mergeSort(arr, 0, 5);

    printArray(arr, 6);
}