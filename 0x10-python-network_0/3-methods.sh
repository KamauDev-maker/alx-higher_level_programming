#!/bin/bash
# Takes in an URL and displays all HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
