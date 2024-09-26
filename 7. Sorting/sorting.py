def bubble_sort(arr):
    size = len(arr)
    itr = 0
    while itr < size:
        for i in range(size-itr-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        itr += 1
    return arr

def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min = i
        for j in range(i+1,size):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def main():
    arr = [11, 64, 12, 25, 22]
    print(bubble_sort(arr=arr))
    print(selection_sort(arr=arr))
if __name__ == "__main__":
    main()