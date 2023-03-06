#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

const request = require('request');
// const characterId = '18';
const apiUrl = process.argv[2];

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const moviesWithWedgeAntilles = JSON.parse(body).results.filter(
    x => x.characters.find(y => y.match(/\/people\/18\/?$/))

    // const moviesWithWedgeAntilles = JSON.parse(body).results.filter(film => {
    //   return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    // }
  );

  console.log(moviesWithWedgeAntilles.length);
});
