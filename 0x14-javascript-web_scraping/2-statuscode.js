#!/usr/bin/node
const request = require('request');
const local = process.argv[2];

request(local, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
