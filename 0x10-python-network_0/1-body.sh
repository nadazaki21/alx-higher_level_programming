#!/bin/bash
# prints the body of the repsonse of requests whose reposnse status is 200.
RESPONSE=$(curl -sI $1 | grep -E " {1}[0-9]{3} {1}"  | cut -d " " -f 2);if [ $RESPONSE == "200" ]; then curl -sXL GET $1; fi
