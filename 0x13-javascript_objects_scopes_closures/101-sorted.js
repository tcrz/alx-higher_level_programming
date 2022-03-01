#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
Object.entries(dict).forEach(([k, v]) => {
  newdict[v] = [];
});
Object.entries(dict).forEach(([k, v]) => {
  newdict[v].push(k);
});
console.log(newdict);
