#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map(function (element, index, obj) {
  return element * index;
});

console.log(list);
console.log(newList);
