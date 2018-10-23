#!/usr/bin/env python3
"""Tests for host_area.__main__."""

import unittest

from host_area.__main__ import main


class TestMain(unittest.TestCase):
    """Tests for host_area.__main__.main."""

    def testEmptyArgs(self):
        """Should return exit status 2 if no arguments are supplied."""
        with self.assertRaises(SystemExit) as cm:
            main([])
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
