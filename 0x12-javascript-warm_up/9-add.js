#!/usr/bin/node
const argv = process.argv.slice(2);
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(argv[0]), parseInt(argv[1])));
