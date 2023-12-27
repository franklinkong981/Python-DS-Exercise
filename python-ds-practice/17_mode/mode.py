def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    max_frequency = None
    max_value = None
    for number in nums:
        if max_frequency == None or nums.count(number) > max_frequency:
            max_frequency = nums.count(number)
            max_value = number
    return max_value
        
