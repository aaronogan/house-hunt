#!/bin/bash

if [ -f /usr/bin/mongod ]; then
  echo "MongoDB is installed on your machine."
  kill -0 "$$" || exit
else
  sudo apt update
  sudo apt install mongodb
  mongodb --version
fi

echo "Script complete."
