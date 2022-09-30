def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key



n = int(input("enter the size of the array"))
arr = []
print("enter {} elements".format(n))
for i in range(n):
        arr.append(int(input()))

print("before sorting\n {}".format(arr))
insertionSort(arr)
print("after sorting\n{}".format(arr))