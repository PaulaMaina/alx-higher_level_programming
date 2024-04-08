#!/usr/bin/node

const { argv } = require('node:process');
let myInt = parseInt(argv[2]);
if (typeof myInt === NaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
