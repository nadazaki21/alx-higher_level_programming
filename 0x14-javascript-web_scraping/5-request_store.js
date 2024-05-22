#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf8', (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing file:', err);
      } else {
        console.log('File written successfully');
      }
    });
  }
});
