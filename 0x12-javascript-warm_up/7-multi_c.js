#!/usr/bin/node
if (typeof (process.argv[2]) === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  const max = parseInt(process.argv[2]);
  for (let i = 0; i < max; i++) {
    console.log('C is fun');
  }
}
