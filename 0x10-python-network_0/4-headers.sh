#!/bin/bash
# This script sends a GET request to the URL passed as an argument and dispays
# the response
curl -sH "X-school-User-Id: 98" "$1" 
