def prompt_options() -> int:
    print("ORMUCO Technical Test\nSelect a Test by entering it's corresponding\
 integer :\n" + "*"*55)

    print("1.  Lines Overlap Test(Question A)\n\
2.  Versions Comparisons Test (Question B)\n\
9.  Exit\n\nSelect option : ")

    try:
        return int(input().strip())

    except ValueError:
        print("ERROR : Input must be a valid input as shown above\n")

    return 0


def error_exit(error_count: int):
    print(f"Too many errors generated of count {error_count}\n \
App will now Exit")
    exit()


def lines_overlap(error_count: int):

    return error_count


def main(error_count: int):
    choice: int
    if(error_count < 3):
        choice = prompt_options()
    else:
        error_exit(error_count)

    valid_choices = [1, 2, 9]

    if choice in valid_choices:
        return 1
    else:
        error_count += 1
        print("Invalid Choice Try Again...")
        main(error_count)


if __name__ == "__main__":
    main(0)
