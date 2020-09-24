#!/usr/bin/node
const $ = window.$;
const theUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.ajax({
  url: theUrl,
  dataType: 'text',
  success: function (result) {
    let name = JSON.parse(result);
    name = name.name;
    $('#character').text(name);
  }
});
