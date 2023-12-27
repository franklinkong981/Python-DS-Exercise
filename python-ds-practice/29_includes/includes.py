def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, list):
        list_to_search = []
        if start == None:
            list_to_search = collection
        else:
            list_to_search = collection[start:]
        if sought in list_to_search:
            return True
        return False
    elif isinstance(collection, str):
        string_to_search = ''
        if start == None:
            string_to_search = collection
        else:
            string_to_search = collection[start:]
        if sought in string_to_search:
            return True
        return False
    elif isinstance(collection, tuple):
        tuple_to_search = ()
        if start == None:
            tuple_to_search = collection
        else:
            tuple_to_search = collection[start:]
        if sought in tuple_to_search:
            return True
        return False
    elif isinstance(collection, set):
        if sought in collection:
            return True
        return False
    elif isinstance(collection, dict):
        if sought in list(collection.values()):
            return True
        return False
    else:
        return None