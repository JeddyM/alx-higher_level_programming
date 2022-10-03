#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
}
let indicator = '';
for (let i = 0; i < num; i++) {
  for (let j = 0; j < num; j++) {
    indicator += 'X';
  }
  console.log(indicator);
  indicator = '';
}
