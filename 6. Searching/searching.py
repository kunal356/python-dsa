def linear_search(arr, k):
    size = len(arr)
    for i in range(size):
        if arr[i] == k:
            return i
    return -1


def binary_search(sorted_arr, k):
    size = len(sorted_arr)
    start = 0
    end = size-1
    while start <= end:
        mid = (start+end)//2
        if sorted_arr[mid] == k:
            return mid
        elif sorted_arr[mid] > k:
            end = mid - 1
        elif sorted_arr[mid] < k:
            start = mid + 1
    return -1


def main():
    arr = [1, 21, 11, 2, 55, 15, 99]
    sorted_arr = [1, 2, 11, 15, 21, 55, 99]
    print("The element is present at index: ", linear_search(arr, 91))
    print("The element is present at index: ",
          binary_search(sorted_arr=sorted_arr, k=2))


if __name__ == "__main__":
    main()
