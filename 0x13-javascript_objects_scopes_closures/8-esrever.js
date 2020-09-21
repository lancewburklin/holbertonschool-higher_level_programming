#!/usr/bin/node
exports.esrever = function (list) {
  class Newlist {
    constructor () {
      this.Thelist = [];
    }
  }
  let idx = list.length - 1;
  let n = 0;
  for (let aList = new Newlist(); idx >= 0; idx--, n++) {
    aList.Thelist[n] = list[idx];
    if (idx === 0) {
      return (aList.Thelist);
    }
  }
};
