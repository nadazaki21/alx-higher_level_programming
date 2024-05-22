#!/usr/bin/node
const request = require('request');
const filmsAPI = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

async function fetchCharacterNames () {
  try {
    const response = await requestPromise(filmsAPI);
    const data = JSON.parse(response.body);
    const charURLs = data.characters;

    const names = await Promise.all(
      charURLs.map(async (url) => {
        const characterResponse = await requestPromise(url);
        const characterData = JSON.parse(characterResponse.body);
        return characterData.name;
      })
    );

    for (const name of names) {
      console.log(name);
    }
  } catch (error) {
    console.error(error);
  }
}

fetchCharacterNames();

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res) => {
      if (err) {
        reject(err);
      } else {
        resolve(res);
      }
    });
  });
}
