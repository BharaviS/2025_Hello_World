def merge_sort(array_s):
    if len(array_s) > 1:
        mid = len(array_s) // 2

        left_half = array_s[:mid]
        right_half = array_s[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_s[k] = left_half[i]
                i += 1
            else:
                array_s[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array_s[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array_s[k] = right_half[j]
            j += 1
            k += 1

array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", array)
merge_sort(array)
print("Sorted array:  ", array)