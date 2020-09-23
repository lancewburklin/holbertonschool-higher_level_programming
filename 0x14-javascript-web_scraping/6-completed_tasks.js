#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const theList = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0,
      10: 0
    };
    const info = JSON.parse(body);
    for (let i = 0; i < info.length; i++) {
      if (info[i].completed === true) {
        const idx = info[i].userId.toString();
        theList[idx] = theList[idx] + 1;
      }
    }
    const items = Object.keys(theList);
    for (let n = 0; n < items.length; n++) {
      if (theList[items[n]] === 0) {
        delete theList[items[n]];
      }
    }
    console.log(theList);
  }
});
