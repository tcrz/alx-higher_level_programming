#!/usr/bin/node
/*
script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
*/
const fs = require('fs');
const argv = process.argv.slice(2);

fs.writeFile(argv[0], argv[1], err => {
  if (err) {
    console.log(err);
  }
});
