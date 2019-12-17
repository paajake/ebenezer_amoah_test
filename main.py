from overlap.overlap import is_overlapping


def prompt_options() -> int:
    print("ORMUCO Technical Test\nSelect a Test by entering it's corresponding"
          + " integer :\n" + "*"*55)

    print("1.  Lines Overlap Test (Question A)\n"
          + "2.  Versions Comparisons Test (Question B)\n"
          + "9.  Exit\n\nSelect option : ")

    try:
        return int(input().strip())

    except ValueError:
        print("ERROR : Input must be a valid input as shown above\n")

    return 0


def error_exit(error_count: int):
    print(f"\n\nToo many errors generated of count {error_count}\n"
          + "App will now Exit")
    exit()


def success_exit():
    print(f"\n\nThanks for testing the Modules\n{'*'*20} B Y E ! ! ! {'*'*20}")
    exit()


def lines_overlap(error_count: int):
    if(error_count > 2):
        error_exit(error_count)

    line_1 = list()
    line_2 = list()

    print("Lines Overlap :\n" + "*"*50)

    try:
        for i in range(0, 2):
            line_1.append(float(input(f"Enter the cordinate {i+1} of Line 1: ")))

        for i in range(0, 2):
            line_2.append(float(input(f"Enter the cordinate {i+1} of Line 2: ")))
    except ValueError:
        print("ERROR : A coordinate MUST be a Number\n")
        lines_overlap(error_count + 1)

    overlap = is_overlapping(tuple(line_1), tuple(line_2))

    if overlap is True:
        print(f"\nResults:\n Yes, Line 1 ({line_1[0]},{line_1[1]}) and "
              + f"Line 2 ({line_2[0]},{line_2[1]}) indeed Do Overlap\n\n")
        return main(0)
    elif overlap is False:
        print(f"\nResults:\nNo, Line 1 ({line_1[0]},{line_1[1]}) and "
              + f"Line 2 ({line_2[0]},{line_2[1]}) DO NOT Overlap\n\n")
        return main(0)

    return main(1)


def main(error_count: int):
    choice: int
    if(error_count < 3):
        choice = prompt_options()
    else:
        error_exit(error_count)

    valid_choices = [1, 2, 9]

    if choice in valid_choices:
        if choice == 1:
            lines_overlap(0)
        elif choice == 9:
            success_exit()
    else:
        error_count += 1
        print("\nInvalid Choice Try Again...")
        main(error_count)


if __name__ == "__main__":
    main(0)
