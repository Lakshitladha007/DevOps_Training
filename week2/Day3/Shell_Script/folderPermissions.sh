#!/bin/bash

if [ -z "$1" ]; then
  echo "Error! missing folder"
  exit 1
fi

path=$1

if [ -d "$path" ]; then
    chmod 444 "$path"
    echo "Permissions updated successfully!"
else
    echo "Folder does not exist."
    exit 1
fi