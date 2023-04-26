#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

if (process.argv.length > 2) {
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    // console.log(charactersURL);

    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
