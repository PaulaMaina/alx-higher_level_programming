#!/bin/bash
# This script sends a POST request to the URL passed and dispays the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" 
