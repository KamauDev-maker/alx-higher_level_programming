#!/usr/bin/bash
# sends a request to that url and displays the size of the body
curl -so /dev/null "$1" -w '%{size_download}\n'
