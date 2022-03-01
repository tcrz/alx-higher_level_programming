#!/usr/bin/node
const argv = process.argv.slice(2);
const fs = require('fs');
fs.readFile(argv[0], 'utf8', function (err, data) {
  if (err) throw (err);
  const contents = data;
  fs.readFile(argv[1], 'utf8', function (err, data) {
    if (err) throw (err);
    const contents2 = data;
    fs.appendFile(argv[2], contents + contents2, function (err) {
      if (err) throw (err);
    });
  });
});
