"""Core functions for manipulating host-area TOML data."""

from host_area import HostAreaException


def check_valid_structure(toml_data):
    """Checks that toml_data is correct and parseable host-area data.

    :param toml_data: Python representation of host-area data, e.g. output from
                      toml.load.
    :raises HostAreaException: If the structure is invalid.
    """
    # TOML data is always a Python dict
    for area_name, area_data in toml_data.items():
        if not isinstance(area_data, dict):
            raise HostAreaException(
                "Area data for area '{}' is of wrong type".format(area_name))

        if "hosts" not in area_data:
            raise HostAreaException(
                "Area '{}' does not contain a 'hosts' key".format(area_name))

        hosts = area_data["hosts"]
        if not isinstance(hosts, list):
            raise HostAreaException(
                "Host data for area '{}' is of wrong type".format(area_name))

        # TOML arrays cannot be mixed types
        if len(hosts) > 0 and not isinstance(hosts[0], str):
            raise HostAreaException("Host list for area '{}' does not contain "
                                    "strings".format(area_name))
