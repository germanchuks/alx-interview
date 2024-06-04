#!/usr/bin/node
// Script to print all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const characters = data.characters;
  fetchNextCharacter(characters, 0);
});

const fetchNextCharacter = (characters, index) => {
  if (index === characters.length) return;

  request(characters[index], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    index++;
    fetchNextCharacter(characters, index);
  });
};
