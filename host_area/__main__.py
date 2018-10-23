#!/usr/bin/env python3
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv

    print("Hello World!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
