#!/usr/bin/node
exports.esrever = function (list) {
  let idx = list.length - 1;
  for (let n = 0; idx > n; idx--, n++) {
    const temp = list[n];
    list[n] = list[idx];
    list[idx] = temp;
  }
  return (list);
};
