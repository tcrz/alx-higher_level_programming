#!/usr/bin/node
const argv = process.argv.slice(2);
if (!argv.length) {
  console.log('No argument');
} else if (argv.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
