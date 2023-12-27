def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    numbers_list = []
    while num1 != 0:
        numbers_list.append(num1 % 10)
        num1 = int(num1 / 10)
    while num2 != 0:
        number_to_remove = num2 % 10
        if number_to_remove not in numbers_list:
            return False
        index_to_remove = numbers_list.index(number_to_remove)
        numbers_list.pop(index_to_remove)
        num2 = int(num2 / 10)
    if len(numbers_list) != 0:
        return False
    return True 