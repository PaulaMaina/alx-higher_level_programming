#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2).map(Number);
  console.log(nums.sort((i, j) => j - i)[1]);
}
