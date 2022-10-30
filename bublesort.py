def bublesort(element):
    swapped = False

    #loop
    for n in range(len(element)-1,0,-1):
        for i in range(n):
            if element[i] > element[i+1]:
                swapped = True
                element[i], element[i + 1] = element[i + 1], element[i]
        if not swapped:
            return

element = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is,")
print(element)
bublesort(element)
print("Sorted Array is, ")
print(element)

