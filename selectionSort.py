def selectionSort(a, s):
    for ind in range(s):
        min_index = ind

        for j in range(ind + 1, s):
            if a[j] < a[min_index]:
                min_index = j
        (a[ind], a[min_index]) = (a[min_index], a[ind])

arr = [1, 45, 0, 11, 10,88,-9,-20,74]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
