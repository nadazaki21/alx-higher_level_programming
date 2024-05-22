#!/usr/bin/node

const request = require('request');

const api = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2] ;

request(api , (err, res) => {
    if (err) {
        console.log(err);
    } else {
        //console.log(api);
        data  = res.body
        console.log(JSON.parse(data).title);
    }
})
