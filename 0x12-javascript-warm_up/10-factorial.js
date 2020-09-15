#!/usr/bin/node
function findFactorial (mult, num) {
  if (isNaN(mult) || isNaN(num)) {
    console.log(1);
    return;
  }
  if (mult !== 0) {
    findFactorial(mult - 1, num * mult);
  } else {
    console.log(num);
  }
}
findFactorial(parseInt(process.argv[2]) - 1, parseInt(process.argv[2]));
