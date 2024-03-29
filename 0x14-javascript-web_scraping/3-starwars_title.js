#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
