# host-area-challenge

## Challenge description (as provided)
Let's model a system where you have areas, and hosts within areas.
These are described in a toml file. A host can only be in an area.
How can you check that a document following this schema does not have the same hosts in different areas.

For example this is invalid because host2 is in both areas.
```
[area1]
hosts = ['host1', 'host2']
[area2]
hosts = ['host2','host3']
```

## Functional requirements
- [x] Read toml file and convert to internal representation
- [x] Validate internal representation and reject invalid configurations
- [x] Check that hosts are only assigned to a single area
- [x] Report to the user on pass/fail
- [x] Have a -q flag to suppress output
- [x] Return appropriate error codes for use in scripts

## Other requirements
- [x] Proper project structure (setuptools)
- [x] Manage any dependencies
- [x] Well defined entry point and CLI
- [x] Should be easily deployable
- [x] Testing
- [ ] Logging

## Notes
* In the provided example I have uncapitalised the "hosts" key as TOML is case-sensitive.
  I am assuming that a host-area TOML file with a capitalised "hosts" key is invalid.
