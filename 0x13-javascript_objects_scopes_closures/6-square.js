#!/usr/bin/node
const Squareprint = require('./5-square');

module.exports = class Square extends Squareprint {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(Array(this.height + 1).join(c));
      }
    }
  }
};
