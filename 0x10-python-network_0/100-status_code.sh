#!/bin/bash
# This script sends a request to the URL passed & displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
