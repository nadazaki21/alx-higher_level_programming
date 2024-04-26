#!/bin/bash
#curl  -ws "%{size_download}"  "$1"
curl -s --head $1 | grep Content-Length | cut -d " " -f 2
