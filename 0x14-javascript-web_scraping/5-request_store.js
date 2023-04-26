#!/usr/bin/node

/*
A script that gets the contents of a webpage and stores it in a file.
  The first argument is the URL to request
  The second argument the file path to store the body response
  The file must be UTF-8 encoded
  You must use the module request
*/

const fs = require('fs');
const request = require('request');
const requestURL = process.argv[2];
const filePath = process.argv[3];

// Using params/options to pass to our request func.
const options = {
  url: requestURL,
  // method: 'GET',
  qs: {} // pass you key value pair of your query string

};

request.get(options, 'utf-8', (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
