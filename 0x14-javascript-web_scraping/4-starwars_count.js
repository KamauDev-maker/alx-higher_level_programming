#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      if (characters.indexOf(`https://swapi-api.alx-tools.com/api/people/${characterId}/`) !== -1) {
        count++;
      }
    }
    console.log(`${count}`);
  } else {
    console.log('Error:', error);
  }
});
