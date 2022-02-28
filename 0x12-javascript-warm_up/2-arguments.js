#!/usr/bin/node
const argv = process.argv.slice(2);
if (!argv.length) { console.log('No Argument'); } else if (argv.length === 1) { console.log('Argument Found'); } else { console.log('Arguments Found'); }
