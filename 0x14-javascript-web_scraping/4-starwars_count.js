#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
	if (error) {
		console.log(error);
	} else if (response.statusCode == 200) {
		const films = JSON.parse(body).results;
		let count = 0;
		for (const film in films) {
			const filmChars = films[film].characters;
			for (const charIndex in filmChars) {
				if (filmChars[charsIndex].includes('18')) {
					count++;
				}
			}
		}
		console.log(count);
	} else {
		console.log('An error occured. Status code: ' + response.statusCode);
	}
});
