

def mergeSort(arr):
    """
    Merge Sort Algorithm (Based from https://www.geeksforgeeks.org/merge-sort/).

    :param list arr: List of unsorted integers
    """
    if len(arr) > 1:

        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array elements into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the first half
        mergeSort(left)

        # Sorting the second half
        mergeSort(right)

        # i track the index of left variable (the left side array)
        # j track the index of right variable (the right side array)
        # k track the index of arr variable (the sorting array)
        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element left behind
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

