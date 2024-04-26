#!/bin/bash
curl  -w "%{size_download}"  "$1"
