import argparse
from typing import Sequence

from src.filename_length_check import supporting_functions


def main(argv: Sequence[str] | None = None) -> int:
    """
    CLI entrypoint.

    Parameters
    ----------
    argv : Sequence[str] | None
           Command line arguments.

    Returns
    ----------
    int
    1 if the check finds a problem, otherwise 0
    """
    parser = argparse.ArgumentParser(prog='validate-filename-length')
    parser.add_argument(
        name='--filenames',
        nargs='*',
        help='Filenames to process.',
    )
    parser.add_argument(
        name='--min-len',
        required=False,
        default=3,
        help='The minimum allowed length for filenames.',
    )
    parser.add_argument(
        name='--max-len',
        required=False,
        default=40,
        help='The maximum allowed length for filenames.',
    )

    args = parser.parse_args(argv)

    results = [
        supporting_functions.is_filename_length_valid(
            filename, args.min_len, args.max_len
        )
        for filename in args.filenames
    ]
    return int(all(results))
