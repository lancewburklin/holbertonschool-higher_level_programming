#!/usr/bin/node
function findLargest (index) {
  const args = process.argv;
  let x = parseInt(args[index]);
  let y = parseInt(args[index]);
  for (let i = index; i < args.length; i++) {
    if (isNaN(parseInt(args[i]))) {
      return (parseInt(args[i]));
    }
    if (x < parseInt(args[i])) {
      y = x;
      x = parseInt(args[i]);
    }
    if (y < parseInt(args[i]) && x !== parseInt(args[i])) {
      y = parseInt(args[i]);
    }
    if (i + 1 === args.length) {
      if (x !== y && index === 2) {
        return (y);
      } else {
        if (index === 2) {
          return (findLargest(3));
        }
      }
    }
  }
  return (x);
}

const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const res = findLargest(2);
  console.log(res);
}
