def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_as_list = list(phrase)
    swap_list = [char.swapcase() if char.upper() == to_swap or char.lower() == to_swap else char for char in phrase_as_list]
    return "".join(swap_list)
