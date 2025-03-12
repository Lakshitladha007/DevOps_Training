#!/bin/bash

if [ -z "$1" ]; then
  echo "Error! missing file or folder path"
  exit 1
fi

path=$1

if [ -e "$path" ]; then
    chmod 666 "$path"
    echo "Permissions updated successfully!"
else
    echo "File or folder does not exist."
    exit 1
fi

