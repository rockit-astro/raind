## W1m rain detector daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/diskspaced.svg?branch=master)](https://travis-ci.org/warwick-one-metre/diskspaced)

Part of the observatory software for the Warwick one-meter telescope.

`raind` recieves data from [a custom rain-detector unit](https://github.com/warwick-one-metre/raindetector) and
makes the latest measurement available for other services via Pyro.

`rain` is a commandline utility that prints the latest measurement in a human-readable form.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `onemetre-raindetector-server`, the `raind` must be enabled using:
```
sudo systemctl enable raind.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start raind.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9017/tcp --permanent
sudo firewall-cmd --reload
```

### Hardware Setup

The [rain-detector unit](https://github.com/warwick-one-metre/raindetector) is matched against its unique serial number.  If the Arduino is replaced then the serial number should be updated in `10-onemetre-rain.rules`.
