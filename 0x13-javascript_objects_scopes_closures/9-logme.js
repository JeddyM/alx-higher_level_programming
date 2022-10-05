#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
  function print (item) {
    console.log(num + ': ' + item);
    num++;
  }
  print(item);
};
