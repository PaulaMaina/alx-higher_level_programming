#!/bin/bash
# This script displays the HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
