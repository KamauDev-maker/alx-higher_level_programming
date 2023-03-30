#!/bin/bash
# Sends a Delete request to the URL passed as the first arguments
curl -s "$1" -X DELETE
