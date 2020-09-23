#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const fileName = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body.toString('utf8'), function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
