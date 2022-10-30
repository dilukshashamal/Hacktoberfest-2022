def insertionSort(array):

    for i in range(1,len(array)):
        key = array[i]

        j = i-1
        while j >=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

arr = [12,45,4,35,8,9,75]
insertionSort(arr)
lst = []
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)