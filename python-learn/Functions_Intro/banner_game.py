def banner_text(strings: str = " ", screen_width: int = 80) -> None:
    """
    Creates a centered - bordered `str` that would function as a banner

    :param strings: string to print.
    An asterisk (*) will result in a row of asterisks.
    The default will print a blank line, with a ** border at
    the left and right edges.
    :param screen_width: The overall width to print within
    (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(strings) > screen_width - 4:
        raise ValueError("String {0} is larger"
                         "than specified width {1}"
                         .format(strings, screen_width))

    if strings == "*":
        print("*" * screen_width)
    else:
        print("**{}**"
              .format(strings.center(screen_width - 4)))


banner_text("*", 60)
banner_text("SYALALALALLALALA", 60)
banner_text(screen_width=60)
banner_text("*", 60)