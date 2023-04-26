#!/usr/bin/node

/*
A script that prints the number of movies where the character “Wedge Antilles” is present.
  The first argument is the API URL of the Star wars API:
    `https://swapi-api.alx-tools.com/api/films/`
  Wedge Antilles is character ID 18
    The script must use this ID for filtering the result of the API
  You must use the module request
*/

const request = require('request');
// const qs = require('qs');
const apiURL = process.argv[2];

// const options = {
//   url:apiURL,
//   method:'GET',
//   qs:{
//     characters:"https://swapi-api.alx-tools.com/api/people/18/"
//   }
// }

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const movies = JSON.parse(body).results; // returns a list of movies
  let count = 0;
  // const films18 = movies.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`))
  // console.log(films18.length)
  movies.forEach(movie => {
    const pattern = /\/people\/18\/?$/; // /people/18 with / optional $ marks from end of string
    if (movie.characters.find(character => character.match(pattern))) {
      count++;
    }
  });
  console.log(count);
});
