#!/usr/bin/node
let log = 0;
exports.logMe = function (item) {
  console.log(log + ':', item);
  log++;
};
