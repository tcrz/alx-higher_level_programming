/*
Script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML tag UL#list_movies
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const results = data.results;
  results.forEach(result => {
    $('UL#list_movies').append($('<li></li>').text(result.title));
  });
});
