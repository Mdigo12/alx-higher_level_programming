#!/usr/bin/node
/*
a script that reads and prints the content of a file
The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
*/

const fs = require('fs');
const filePath = process.argv[2]; // get file path from command line

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
