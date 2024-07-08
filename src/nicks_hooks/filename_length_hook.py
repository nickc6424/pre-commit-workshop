"""Functions to support the filename length hook."""

from pathlib import Path


def is_filename_length_valid(filename: str, min_length: int, max_length: int) -> int:
    """
    Check if a filename length is valid.

    Parameters
    ----------
    filename : str
               The name of the file to be checked.
    min_length : int
                 The minimum permitted length.
    max_length : int
                 The maximum permitted length.

    Returns
    ----------
    is_valid: bool
              True if valid, False if invalid.
    """
    filename_length = len(Path(filename).stem)
    too_long = filename_length > max_length
    too_short = filename_length < min_length
    if too_long or too_short:
        issue_desc = 'too_long' if too_long else 'too_short'
        print(
            f"The length of the name of file '{filename}' is {filename_length}, which is {issue_desc}."
        )
        print(
            f'The length of a filename should be between {min_length} and {max_length}.'
        )
        return False
    return True
