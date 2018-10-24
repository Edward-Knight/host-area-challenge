#!/usr/bin/env python3
"""Validates host-area TOML configuration files."""
import argparse
import sys

import toml

import host_area


def main(argv=None):
    """
    Main entry point.

    :param argv: List of command line arguments. If None, will use sys.argv[1:].
    """
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="host_area", description=__doc__)
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + host_area.__version__)
    parser.add_argument("file", type=open,
                        help="TOML file to validate")
    args = parser.parse_args(argv)

    print("Hello World!")


if __name__ == "__main__":
    main()
