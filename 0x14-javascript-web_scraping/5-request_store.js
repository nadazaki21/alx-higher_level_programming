#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file_path = process.argv[3];

request(url,"utf8", (error, response, body) => {
    try{

        fs.writeFile(file_path, body, 'utf8', (err) => {
            if (err) {
                console.error(err);
            }
        });

    }
    catch(error){
        console.log(error);
    }
})
