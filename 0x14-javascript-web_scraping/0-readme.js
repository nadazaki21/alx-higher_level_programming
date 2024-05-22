#!/usr/bin/node
const fs = require('fs');

/* reading a file asynchronously */
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
