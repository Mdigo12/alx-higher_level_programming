#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the movie endpoint
request.get(movieUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body);

  // If it matches, print the movie title
  console.log(movie.title);
});
