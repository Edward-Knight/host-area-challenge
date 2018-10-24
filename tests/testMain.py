#!/usr/bin/env python3
"""Tests for host_area.__main__."""

from os.path import join
import unittest

from host_area.__main__ import main
from tests import TEST_DATA_DIR


class TestExitStatus(unittest.TestCase):
    """Tests the exit status of host_area.__main__.main."""

    def testEmptyArgs(self):
        """Should exit with status 2 if no arguments are supplied."""
        with self.assertRaises(SystemExit) as cm:
            main([])
        self.assertEqual(cm.exception.code, 2)

    def testIOError(self):
        """Should exit with status 5 if there is an I/O error."""
        with self.assertRaises(SystemExit) as cm:
            main(["nothing"])
        self.assertEqual(cm.exception.code, 5)

    def testNonTOML(self):
        """Should exit with status 1 if presented with a non-TOML file."""
        with self.assertRaises(SystemExit) as cm:
            main(["requirements.txt"])
        self.assertEqual(cm.exception.code, 1)

    def testInvalidTOML(self):
        """Should exit with status 1 if presented with an invalid host-area
        file.
        """
        with self.assertRaises(SystemExit) as cm:
            main([join(TEST_DATA_DIR, "invalid-example.toml")])
        self.assertEqual(cm.exception.code, 1)

    def testValidTOML(self):
        """Should exit with status 0 if presented with a valid host-area
        file.
        """
        with self.assertRaises(SystemExit) as cm:
            main([join(TEST_DATA_DIR, "valid-example.toml")])
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
