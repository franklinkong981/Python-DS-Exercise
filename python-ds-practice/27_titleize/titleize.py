def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list_of_chars = list(phrase)
    current_index = 0
    for char in list_of_chars:
        if current_index == 0 or list_of_chars[current_index - 1] == ' ':
            list_of_chars[current_index] = list_of_chars[current_index].upper()
        else:
            list_of_chars[current_index] = list_of_chars[current_index].lower()
        current_index += 1
    return "".join(list_of_chars)
