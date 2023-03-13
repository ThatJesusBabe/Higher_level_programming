#!/usr/bin/node
const args = process.argv.slice(2); // slice off the first two elements of the array

if (args.length >= 2) {
  const [arg1, arg2] = args;
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log('undefined is undefined');
}
