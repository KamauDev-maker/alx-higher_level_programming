#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log('code: ', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    let count = 0;
    for (const film of jsonBody.results) {
      for (const character of film.characters) {
        if (character.endswith('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
