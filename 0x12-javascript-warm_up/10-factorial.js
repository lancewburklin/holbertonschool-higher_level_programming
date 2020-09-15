#!/usr/bin/node
function findFactorial (mult, num) {
  if (mult < 1) {
    return (num);
  }
  return (findFactorial(mult - 1, num * mult));
}
if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  const args = process.argv;
  console.log(findFactorial(parseInt(args[2]) - 1, parseInt(args[2])));
}
