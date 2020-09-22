#!/usr/bin/node
const request = require('request');
const location = process.argv[2];

request(location, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (let i = 0; i < data.results.length; i++) {
      for (let n = 0; n < data.results[i].characters.length; n++) {
        if (data.results[i].characters[n].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
