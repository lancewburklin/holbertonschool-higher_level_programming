#!/usr/bin/node
if (typeof (process.argv[2]) !== 'undefined') {
  const newNum = parseInt(process.argv[2]);
  if (isNaN(newNum) === false) {
    console.log('My number: ' + newNum);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
