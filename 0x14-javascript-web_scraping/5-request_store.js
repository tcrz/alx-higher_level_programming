#!/usr/bin/node
/*
script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request

The second argument the file path to store the body response

The file must be UTF-8 encoded

 must use the module request
*/
const request = require('request');
const fs = require('fs');
const argv = process.argv.slice(2);

request(argv[0]).pipe(fs.createWriteStream(argv[1]));
