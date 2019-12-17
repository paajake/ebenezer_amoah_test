def compare(version_1: str, version_2: str) -> int:
    """
    A versions comparator.
    This function takes in two version numbers as strings of the form `1.1`
    and returns an integer, based on how they compare to each other.

    Parameters:
    version_1 (str): This a string of the first version number.

    version_2 (str): This a string of the first version number.

    Returns:
    int: Returns 1, if version_1 is greater than version_2,
    or returns 0, if version_1 is equal to version_2,
    or returns -1 if version 1 is less than version_2,
    else returns 404 if an answer wasn't found.

    Examples:
    >>> compare("1.0","0.1")
    1
    >>> compare("0.1","0.1.0")
    0
    >>> compare("1.1","2.0")
    -1
    """
    version_1 = version_1.strip()
    version_2 = version_2.strip()

    if version_1 == version_2:
        return 0

    version_1_list = [int(val) for val in version_1.split('.')]
    version_2_list = [int(val) for val in version_2.split('.')]

    i = 0

    while i < len(version_1_list) and i < len(version_2_list):

        if version_1_list[i] > version_2_list[i]:
            return 1
        elif version_2_list[i] > version_1_list[i]:
            return -1

        i += 1

    if i < len(version_1_list):
        if sum(version_1_list[i:]) > 0:
            return 1
        else:
            return 0

    elif i < len(version_2_list):
        if sum(version_2_list[i:]) > 0:
            return -1
        else:
            return 0

    return 404


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
