#!/bin/bash
RESPONSE=$(curl -sI $1 | grep HTTP | cut -d " " -f 2); if [ $RESPONSE == "200" ]; then curl -s $1; fi
