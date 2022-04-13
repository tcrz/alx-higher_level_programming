#!/usr/bin/node
/*
script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request
"""
*/
const request = require('request');
const argv = process.argv.slice(2);

const endpoint = 'https://swapi-api.hbtn.io/api/films/' + argv[0];

request(endpoint, function (error, respose, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).characters.forEach(url => {
      request(url, function (error, respose, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
