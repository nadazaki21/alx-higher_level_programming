#!/usr/bin/node
if (Math.floor(Number(process.argv[2])) === parseInt(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
