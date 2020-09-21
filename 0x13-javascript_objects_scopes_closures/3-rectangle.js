#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let n = 0; n < this.width; n++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
