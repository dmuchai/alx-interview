#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;

  // Use a helper to fetch and print characters sequentially
  const printCharacters = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (err, res, body) => {
      if (err) return console.error(err);
      const name = JSON.parse(body).name;
      console.log(name);
      printCharacters(index + 1);
    });
  };

  printCharacters(0);
});
