#!/usr/bin/node

const nums = process.argv.slice(2);

if (nums.length <= 3) {
  console.log(0);
} else {
  console.log(nums.map(num => parseInt(num)).sort((i, j) => j - i)[1]);
}
