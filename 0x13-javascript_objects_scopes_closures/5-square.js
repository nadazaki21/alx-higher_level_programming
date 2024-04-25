#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = class Sqaure extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
