#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let step = 0; step < this.height; step++) {
      for (let step = 0; step < this.width; step++) {
        str += 'X';
      }
      console.log(str);
      str = '';
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
};
