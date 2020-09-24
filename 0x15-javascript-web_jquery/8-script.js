#!/usr/bin/node
const $ = window.$;
const theUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.ajax({
  url: theUrl,
  dataType: 'text',
  success: function (result) {
    let results = JSON.parse(result);
    results = results.results;
    for (let i = 0; i < results.length; i++) {
      const title = results[i].title;
      const foo = $('<li></li>').text(title);
      $('#list_movies').append(foo);
    }
  }
});
