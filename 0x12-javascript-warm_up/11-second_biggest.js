#!/usr/bin/node

const args = process.argv;
const nums = args.slice(2);

if (nums.length <= 3) {
  console.log(0);
} else {
  nums.sort();
  console.log(nums[nums.length - 2]);
}
