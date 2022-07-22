## W1m rain detector daemon

`raind` checks the output from a set of IR rain detectors and
makes the latest measurement available for other services via Pyro.
It is set up manually on a Raspberry Pi.

`rain` is a commandline utility that prints the latest measurement in a human-readable form.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

