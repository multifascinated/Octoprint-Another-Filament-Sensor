#!/bin/bash

SCRIPT_DIR=$(dirname $(realpath $0))
rsync -a --exclude='.*.swp' ${SCRIPT_DIR}/octoprint_filamentsensorng/ \
  /home/pi/oprint.gauss/lib/python2.7/site-packages/octoprint_filamentsensorng
