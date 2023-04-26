#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const WEDGE_ANTILLES_ID = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const wedgeMovies = movies.filter(movie => movie.characters.include(WEDGE_ANTILLES_ID));
    const countWedgeMovies = wedgeMovies.lenght;
    console.log(`Wedge Antilles appears in ${countWedgeMovies} movies.`);
  }
});
