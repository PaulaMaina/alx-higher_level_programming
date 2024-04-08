#!/usr/bin/node

const { argv } = require('node:process');
const myInt = parseInt(argv[2]);
if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
