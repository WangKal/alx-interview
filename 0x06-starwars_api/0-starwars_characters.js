#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
  starWarsCharacters(characters, 0);
  }
});

function starWarsCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        starWarsCharacters(characters, index + 1);
      }
    }
  });
}
