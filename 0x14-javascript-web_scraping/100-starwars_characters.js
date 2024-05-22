#!/usr/bin/node
const request = require('request');
const films_api = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];


request(films_api, (err, res) => {
    if (err) {
        console.log(err);
    } else {
        const data = JSON.parse(res.body);
        const characters_urls = data.characters;
        //console.log(characters_urls);
        
        for (let i = 0; i < characters_urls.length; i++) {
            //console.log(characters_urls[i]);
            request(characters_urls[i], (err, res) => {
                if (err) {
                    console.log(err);
                } else {
                    const data = JSON.parse(res.body);
                    console.log(data.name);
                }
            })
        }
        
    }
})
