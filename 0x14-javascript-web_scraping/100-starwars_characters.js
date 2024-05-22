#!/usr/bin/node
const request = require('request');
const filmsAPI = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(filmsAPI, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(res.body);
    const charURLs = data.characters;
    // console.log(charURLs);

    for (let i = 0; i < charURLs.length; i++) {
      // console.log(charURLs[i]);
      request(charURLs[i], (err, res) => {
        if (err) {
          console.log(err);
        } else {
          const data = JSON.parse(res.body);
          console.log(data.name);
        }
      });
    }
  }
});
