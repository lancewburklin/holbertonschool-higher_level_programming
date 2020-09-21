#!/usr/bin/node
const Cheese = require('./5-square');

module.exports = class Square extends Cheese {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let n = 0; n < this.width; n++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
