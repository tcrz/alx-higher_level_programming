#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(parseInt(argv[0]))) {
  console.log('Missing number of occurrences');
} else {
  for (let step = parseInt(argv[0]); step > 0; step--) {
    console.log('C is fun');
  }
}
