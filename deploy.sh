#!/bin/bash

# Create service descriptor file in /etc/systemd/system/
sudo cp *.service /etc/systemd/system/

# Reload service configuration
sudo systemctl daemon-reload

# Enable starting the service on system boot with the following command
# sudo systemctl enable wesearch

# You can also stop and start the service manually at any moment with the following commands, respectively:
# sudo service wesearch start
# sudo service wesearch stop
