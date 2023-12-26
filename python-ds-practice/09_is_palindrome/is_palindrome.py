def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_without_spaces = "".join(phrase.split(" "))
    phrase_without_spaces = phrase_without_spaces.lower()
    phrase_as_list = list(phrase_without_spaces)
    phrase_as_list.reverse()
    phrase_backwards = "".join(phrase_as_list)
    return phrase_without_spaces == phrase_backwards
