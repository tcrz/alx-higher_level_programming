#!/usr/bin/node
const argv = process.argv.slice(2);
function factorial (a) {
  if (a <= 0 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(parseInt(argv[0])));
