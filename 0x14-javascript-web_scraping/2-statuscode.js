#!/usr/bin/node
/*
script that display the status code of a GET request using the requests module
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
*/
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
