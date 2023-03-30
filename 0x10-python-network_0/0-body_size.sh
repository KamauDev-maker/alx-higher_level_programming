#!/bin/bash
# sends a request to that url and displays the size of the body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
