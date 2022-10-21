# Recursive's solution fir factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# MergeSort arrays
def mergeSort(arr):
    if len(arr) > 1:
        # Spliting to one number
        print('splitting ', arr)
        mid = len(arr) / 2
        left = arr[:int(mid)]
        right = arr[int(mid):]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        # Merging between subarrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    print("merging ", arr)
    return arr


if __name__ == "__main__":
    print(factorial(4))
    print(mergeSort([356, 97, 846, 215, 547, 985]))
