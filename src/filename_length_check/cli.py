import argparse
from sys import argv
from typing import Sequence

import supporting_functions


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
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )
    parser.add_argument(
        '--min-len',
        default=3,
        type=int,
        help='The minimum allowed length for filenames.',
    )
    parser.add_argument(
        '--max-len',
        default=40,
        type=int,
        help='The maximum allowed length for filenames.',
    )

    args = parser.parse_args(argv)

    results = [
        supporting_functions.is_filename_length_valid(
            filename, args.min_len, args.max_len
        )
        for filename in args.filenames[1:]
    ]
    return int(all(results))


if __name__ == '__main__':
    main(argv)
