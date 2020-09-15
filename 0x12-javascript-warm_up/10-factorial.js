#!/usr/bin/node
function findFactorial (mult, num) {
  if (mult !== 0) {
    findFactorial(mult - 1, num * mult);
  } else {
    console.log(num);
  }
}
if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  findFactorial(parseInt(process.argv[2]) - 1, parseInt(process.argv[2]));
}
