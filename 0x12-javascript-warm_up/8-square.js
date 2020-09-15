#!/usr/bin/node
const newNum = parseInt(process.argv[2]);
if (isNaN(newNum)) {
  console.log('Missing size');
}
let sqr = 'X';
for (let n = 1; n < newNum; n++) {
  sqr = sqr + 'X';
}
for (let i = 0; i < newNum; i++) {
  console.log(sqr);
}
