#!/bin/bash
# This script sends a request to the URL passed as an argument and dispays
# the onlythe status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
