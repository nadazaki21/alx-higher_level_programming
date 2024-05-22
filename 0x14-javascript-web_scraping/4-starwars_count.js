#!/usr/bin/node
const request = require('request');
const api = process.argv[2];


let counter = 0;

request(api , (err, res) => {
    if (err) {
        console.log(err);
    } else {
        const data  = res.body
        const arr = JSON.parse(data).results
        for (let i = 0; i < arr.length; i++) {
            const chracters_number = arr[i].characters.length; 
            //console.log(chracters_number, arr[i].characters.length);
            for (let j = 0; j < chracters_number; j++) {
                if (arr[i].characters[j] === "https://swapi-api.alx-tools.com/api/people/18/") {
                   counter = counter + 1;
                   break;
                }
            }
        }
        console.log(counter);
    }
})
