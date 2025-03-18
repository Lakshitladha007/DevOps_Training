#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: missing parameter username."
  exit 1
fi

if id -u "$1" >/dev/null 2>&1; then
    echo "User exists"
else
    echo "User does not exist"
fi