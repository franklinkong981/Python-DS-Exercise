def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    length_of_list = len(lst)
    if length_of_list > 0:
        return lst[length_of_list-1]
    else:
        return None