LOWER_LIMIT = 3
UPPER_LIMIT = 15


def perform_check(filename: str) -> int:
    filename_length = len(filename)
    too_long = filename_length > UPPER_LIMIT
    too_short = filename_length < LOWER_LIMIT
    if too_long or too_short:
        issue_desc = "too_long" if too_long else "too_short"
        print(f"The length of the name of file '{filename}' is {filename_length}, which is {issue_desc}.")
        print(f"The length of a filename should be between {LOWER_LIMIT} and {UPPER_LIMIT}.")
        return 1
    return 0
