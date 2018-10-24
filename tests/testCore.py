#!/usr/bin/env python3
"""Tests for host_area.core."""

import unittest

from host_area import HostAreaException
from host_area.core import check_single_assignment, check_well_formed


class TestCheckWellFormed(unittest.TestCase):
    """Tests for host_area.core.check_well_formed."""

    def testEmptyDict(self):
        """An empty dict is valid host-area data."""
        check_well_formed({})

    def testValidData(self):
        """Test using provided well formed data."""
        toml_data = {
            "area1": {"hosts": ["host1", "host2"]},
            "area2": {"hosts": ["host2", "host3"]}
        }
        check_well_formed(toml_data)

    def testBadAreaData(self):
        """Check bad area data is rejected."""
        toml_data = {
            "area1": ["host1", "host2"]
        }
        self.assertRaises(HostAreaException, check_well_formed, toml_data)

    def testNoHostsKey(self):
        """Check areas with no host key are rejected."""
        toml_data = {
            "area1": {"boasts": ["host1", "host2"]}
        }
        self.assertRaises(HostAreaException, check_well_formed, toml_data)

    def testEmptyHosts(self):
        """An empty list of hosts is valid."""
        toml_data = {
            "area1": {"hosts": []}
        }
        check_well_formed(toml_data)

    def testBadHostData(self):
        """Check host data of the wrong type is rejected."""
        toml_data = {
            "area1": {"hosts": [1]}
        }
        self.assertRaises(HostAreaException, check_well_formed, toml_data)


class TestCheckSingleAssignment(unittest.TestCase):
    """Tests for host_area.core.check_single_assignment."""

    def testEmptyDict(self):
        """An empty dict is valid host-area data."""
        check_single_assignment({})

    def testValidData(self):
        """Test using provided valid data."""
        toml_data = {
            "area1": {"hosts": ["host1", "host2"]},
            "area2": {"hosts": ["host4", "host3"]}
        }
        check_single_assignment(toml_data)

    def testInvalidData(self):
        """Test using provided invalid data."""
        toml_data = {
            "area1": {"hosts": ["host1", "host2"]},
            "area2": {"hosts": ["host2", "host3"]}
        }
        self.assertRaises(HostAreaException, check_single_assignment, toml_data)

    def testDoubleEntry(self):
        """Check that a host assigned to the same area multiple times is
        rejected.
        """
        toml_data = {
            "area1": {"hosts": ["host1", "host2", "host1"]}
        }
        self.assertRaises(HostAreaException, check_single_assignment, toml_data)


if __name__ == "__main__":
    unittest.main()
