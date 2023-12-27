def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    left_index = 0
    right_index = len(s) - 1
    reverse_vowels_string = s
    while left_index < right_index:
        if s[left_index] not in 'AEIOUaeiou':
            left_index += 1
        if s[right_index] not in 'AEIOUaeiou':
            right_index -= 1
        if left_index < right_index and s[left_index] in 'AEIOUaeiou' and s[right_index] in 'AEIOUaeiou':
            reverse_vowels_string = reverse_vowels_string[0:left_index] + s[right_index] + reverse_vowels_string[left_index+1:right_index] + s[left_index] + reverse_vowels_string[right_index+1:]
            left_index += 1
            right_index -= 1
    return reverse_vowels_string 