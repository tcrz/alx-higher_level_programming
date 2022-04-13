#!/usr/bin/node
/*
script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line in the same order of the list “characters” in the /films/ response
You must use the Star wars API
You must use the module request
*/
const request = require('request');
const argv = process.argv.slice(2);

const endpoint = 'https://swapi-api.hbtn.io/api/films/' + argv[0];

function orderedRequest (array, index) {
  if (index === array.length) {
    return;
  }
  request(array[index], function (error, respose, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      orderedRequest(array, index + 1);
    }
  });
}

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const chrList = JSON.parse(body).characters;
    orderedRequest(chrList, 0);
  }
});
