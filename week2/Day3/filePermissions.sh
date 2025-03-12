#!/bin/bash

if [ -z "$1" ]; then
  echo "Error! missing file"
  exit 1
fi

path=$1

if [ -f "$path" ]; then
    chmod 444 "$path"
    echo "Permissions updated successfully!"
else
    echo "File does not exist."
    exit 1
fi

