#!/usr/bin/node
exports.esrever = function (list) {
  let idx = list.length - 1;
  let n = 0;
  for (let aList = []; idx >= 0; idx--, n++) {
    aList[n] = list[idx];
    if (idx === 0) {
      return (aList);
    }
  }
};
