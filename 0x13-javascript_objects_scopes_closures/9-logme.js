#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  function something () {
    console.log(counter + ": " + item);
    counter++;
  }
  return something();
}
