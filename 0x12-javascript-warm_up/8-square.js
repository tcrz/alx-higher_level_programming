#!/usr/bin/node
const argv = process.argv.slice(2);
let str = '';
if (isNaN(parseInt(argv[0]))) {
  console.log('Missing size');
} else {
  for (let step = 0; step < parseInt(argv[0]); step++) {
    for (let step = 0; step < parseInt(argv[0]); step++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
