#!/usr/bin/node
const Rectangle = require('./4-rectangle'); module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let step = 0; step < this.height; step++) {
      for (let step = 0; step < this.width; step++) {
        str += c;
      }
      console.log(str);
      str = '';
    }
  }
};
