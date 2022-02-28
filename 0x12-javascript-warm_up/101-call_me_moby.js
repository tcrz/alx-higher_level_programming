#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let step = 0; step < x; step++) {
    theFunction();
  }
};
