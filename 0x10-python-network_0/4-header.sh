#!/bin/bash
# This script sends a GET request to the URL passed as an argument and dispays
# the response
curl -sH "X-School-User-Id: 98" "$1" 
