#!/bin/bash
# This script sends a JSON POST request to the URL passed as an argument and displays
# the body of the response
curl -s -H "Content-Type: application/json" -d @ "$2" "$1" "http://localhost:5000"
