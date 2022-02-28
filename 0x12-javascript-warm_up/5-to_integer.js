#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(parseInt(argv[0]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(argv[0]));
}
