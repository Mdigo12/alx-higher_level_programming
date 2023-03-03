#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentText = process.argv[3];

fs.writeFile(filePath, contentText, 'utf-8', (err) => {
    if (err){
        console.log(err);
    }
    // else {
    //     console.log('The file ' + filePath +' has been saved with the following content:\n'+ contentText);
    // }
});
