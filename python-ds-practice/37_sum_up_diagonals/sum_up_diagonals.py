def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    diagonal_sum = 0
    left_index_to_add = 0
    right_index_to_add= len(matrix) - 1
    for number_list in matrix:
        diagonal_sum += (number_list[left_index_to_add] + number_list[right_index_to_add])
        left_index_to_add += 1
        right_index_to_add -= 1
    return diagonal_sum 