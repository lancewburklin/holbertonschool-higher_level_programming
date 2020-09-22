#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const info = process.argv[3];

fs.writeFile(file, info, function (err) {
  if (err) {
    console.log(err);
  }
});
