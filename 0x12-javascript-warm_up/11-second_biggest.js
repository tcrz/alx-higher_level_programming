#!/usr/bin/node
const argv = process.argv.slice(2);
if (!argv[0] || argv.length === 1) {
  console.log(0);
} else {
  const descSort = argv.sort((a, b) => b - a);
  console.log(descSort[1]);
}
