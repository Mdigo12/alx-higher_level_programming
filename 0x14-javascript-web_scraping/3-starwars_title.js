#!/usr/bin/node

/*
A script that prints the title of a Star Wars movie
where the episode number matches a given integer
  The first argument is the movie ID
  You must use the Star wars API with the endpoint
    `https://swapi-api.alx-tools.com/api/films/:id`
  You must use the module request
*/

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Sending a GET request to the movieURL
request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const movie = JSON.parse(body); // Parse the body
  console.log(movie.title); // print the movie title
});
