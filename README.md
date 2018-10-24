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
Hosts = ['host2','host3']
```

## Functional requirements
- [x] Read toml file and convert to internal representation
- [ ] Validate internal representation and reject invalid configurations
- [ ] Check that hosts are only assigned to a single area
- [ ] Report to the user on pass/fail
- [ ] Have a -q flag to suppress output
- [x] Return appropriate error codes for use in scripts

## Other requirements
- [x] Proper project structure (setuptools)
- [x] Manage any dependencies
- [x] Well defined entry point and CLI
- [x] Should be easily deployable
- [x] Testing
- [ ] Logging
