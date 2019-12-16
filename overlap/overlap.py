from typing import Union, Tuple

Coordinate = Union[int, float]


def is_overlapping(line_1: Tuple[Coordinate, Coordinate],
                   line_2: Tuple[Coordinate, Coordinate]) -> bool:
    """
    A line overlap comparator.
    This function takes in the start and end coordinates of 2 lines in the x-line plane as tuples, and checks if they
    overlap.

    Parameters : 
    line_1 ( Tuple(int|float, int|float) ): This is a Tuple of 2 numbers representing the 2 x coordinates that form this
                                            line,assumes the first coordinate is lower than the second.
    line_2 ( Tuple(int|float, int|float) ): This is a Tuple of 2 numbers representing the 2 x coordinates that form this
                                            line assumes the first coordinate is lower than the second.

    Returns: 
    bool: Returns True if lines overlap, else it returns False.

    Examples:
    >>> is_overlapping((0,9),(1,8))
    True
    >>> is_overlapping((0,9),(0,8))
    True
    >>> is_overlapping((0,5),(7,15))
    False
    """

    # For Lines to overlap, the end point of the line with lower boundary, needs to exceed the start point of the other.

    lower_bounded_line: Tuple
    higher_bounded_line: Tuple

    if line_1[0] <= line_2[0]:
        lower_bounded_line = line_1
        higher_bounded_line = line_2
    else:
        lower_bounded_line = line_2
        higher_bounded_line = line_1

    if lower_bounded_line[1] > higher_bounded_line[0]:
        return True

    return False
