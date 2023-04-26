#!/usr/bin/node
/*
A script that writes a string to a file
The first argument is the file path
The second argument is the string to write
The content of the file must be read in utf-8
If an error occurred while writing, print the error object
*/

const fs = require('fs');
const filePath = process.argv[2]; // get file path from command line
const contentString = process.argv[3];

fs.writeFile(filePath, contentString, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
