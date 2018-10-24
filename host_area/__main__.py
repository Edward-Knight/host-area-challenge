#!/usr/bin/env python3
"""Validates host-area TOML configuration files."""
import argparse
import sys

import toml

import host_area
from host_area.core import check_well_formed, check_single_assignment


def main(argv=None):
    """Main entry point.

    :param argv: List of command line arguments. If None, will use sys.argv[1:].
    """
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="host_area", description=__doc__,
        epilog="Exit statuses: 0 if file is valid, 1 if file is invalid, "
               "2 if there is an error parsing arguments, "
               "and 5 if there is an I/O error."
    )
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + host_area.__version__)
    parser.add_argument("file",
                        help="TOML file to validate")
    args = parser.parse_args(argv)

    try:
        toml_data = toml.load(args.file)
        check_well_formed(toml_data)
        check_single_assignment(toml_data)
        print(args.file, "is valid")
    except Exception as e:
        # print a helpful error message and exit with an appropriate exit status
        print(parser.prog + ": " + e.__class__.__name__ + ": " + str(e),
              file=sys.stderr)
        if isinstance(e, IOError):
            sys.exit(5)
        else:
            sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
