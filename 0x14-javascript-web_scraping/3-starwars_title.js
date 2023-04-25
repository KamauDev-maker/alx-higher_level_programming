#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const epsNum = parseInt(movieData.episode_id);

  if (epsNum === parseInt(movieId)) {
    console.log(`Title: ${movieData.title}`);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
