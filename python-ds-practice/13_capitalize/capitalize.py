def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_letter_index = 0
    while not phrase[first_letter_index].isalpha():
        first_letter_index += 1
    first_letter_capitalized = phrase[first_letter_index].upper()
    return phrase[0:first_letter_index] + first_letter_capitalized + phrase[first_letter_index+1:]