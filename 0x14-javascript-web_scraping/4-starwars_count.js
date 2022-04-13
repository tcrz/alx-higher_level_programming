#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resultsList = JSON.parse(body).results;
    const chrList = resultsList.map(n => n.characters);
    let count = 0;
    chrList.forEach(function (n) {
      for (let i = 0; i < n.length; i++) {
        if (n[i].includes('18')) {
          count += 1;
        }
      }
    });
    console.log(count);
  }
});
