def custom_merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_part = array[:mid]
        right_part = array[mid:]

        custom_merge_sort(left_part)
        custom_merge_sort(right_part)

        left_index = right_index = array_index = 0

        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] < right_part[right_index]:
                array[array_index] = left_part[left_index]
                left_index += 1
            else:
                array[array_index] = right_part[right_index]
                right_index += 1
            array_index += 1

        while left_index < len(left_part):
            array[array_index] = left_part[left_index]
            left_index += 1
            array_index += 1

        while right_index < len(right_part):
            array[array_index] = right_part[right_index]
            right_index += 1
            array_index += 1

if __name__ == "__main__":
    input_list = [5, 2, 4, 7, 1, 3, 2, 6]
    print("Original array:", input_list)
    custom_merge_sort(input_list)
    print("Sorted array:", input_list)
