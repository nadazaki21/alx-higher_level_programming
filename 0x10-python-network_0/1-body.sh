#!/bin/bash
# prints the body of the repsonse of requests whose reposnse status is 200.
curl -sX GET $1 -L
