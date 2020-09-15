#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let x = parseInt(process.argv[2]);
  let y = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (x < parseInt(process.argv[i])) {
      y = x;
      x = parseInt(process.argv[i]);
    }
    if (i + 1 === process.argv.length) {
      console.log(y);
    }
  }
}
