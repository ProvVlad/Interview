
def sort_min_to_max(array, min_index, max_index):
    """ Function use algoritm 'Merge sorting' and sort array from min to max.
        First step: Recursive division array in half to one elements lists.
        Second step: Pairwise merging elements by 'Merge' function and sort in process
    """
    # Check how much elements in part of array. If one -> return
    if (max_index - min_index) <= 1:
        return None
    # FInd index of middle of part of array
    mid_index = (max_index + min_index) // 2

    # Functions recursive division array to left and right parts
    sort_min_to_max(array, min_index, mid_index)
    sort_min_to_max(array, mid_index, max_index)
    # Merging parts of array and sort in process
    merge(array, min_index, max_index, mid_index)
    

def merge(array, min_index, max_index, mid_index):
    """ Function Pairwise merging elements and sort in process"""
    
    # Create copies of left and right parts and indexes for iteration
    left_copy = array[min_index : mid_index]    
    left_index = 0
    right_copy = array[mid_index : max_index]
    right_index = 0
    # Index of array to rewrites elements. Start from the left
    sort_index = min_index

    # Compare elements from left and right copies starting from the left
    # Write min element to array. Finish when elements in left or right copies will end 
    while left_index < len(left_copy) and right_index < len(right_copy):
        
        if left_copy[left_index] < right_copy[right_index]:
            array[sort_index] = left_copy[left_index]
            left_index = left_index + 1
        else:
            array[sort_index] = right_copy[right_index]
            right_index = right_index + 1

        sort_index = sort_index + 1

    # Added remaining elements of left or right copies
    while left_index < len(left_copy):
        array[sort_index] = left_copy[left_index]
        left_index = left_index + 1
        sort_index = sort_index + 1

    while right_index < len(right_copy):
        array[sort_index] = right_copy[right_index]
        right_index = right_index + 1
        sort_index = sort_index + 1



def test_sort_min_to_max():
    """ Unittests for function 'sort_min_to_max'."""

    test_list = []
    sort_min_to_max(test_list, 0, len(test_list))
    assert test_list == [], 'Wrong answer: {}'.format(test_list)

    test_list = [-5]
    sort_min_to_max(test_list, 0, len(test_list))
    assert test_list == [-5], 'Wrong answer: {}'.format(test_list)

    test_list = [10, 10, 10, 10, 10]
    sort_min_to_max(test_list, 0, len(test_list))
    assert test_list == [10, 10, 10, 10, 10], 'Wrong answer: {}'.format(test_list)

    test_list = [10, 1, 7, -2, 45, -10, 100, 1, 15, -25, 0]
    sort_min_to_max(test_list, 0, len(test_list))
    assert test_list == [-25, -10, -2, 0, 1, 1, 7, 10, 15, 45, 100], 'Wrong answer: {}'.format(test_list)

    test_list = [6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
    sort_min_to_max(test_list, 0, len(test_list))
    assert test_list == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6], 'Wrong answer: {}'.format(test_list)

    print('All tests passed')

  




if __name__ == "__main__":
    test_sort_min_to_max()


