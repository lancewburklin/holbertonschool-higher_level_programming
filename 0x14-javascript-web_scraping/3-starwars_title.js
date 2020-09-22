#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/' + num;

request(api, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const title = JSON.parse(body);
    console.log(title.title);
  }
});
