#!/usr/bin/node
function secondLargest (myArray) {
  if (myArray.length === 2 || myArray.length === 3) {
    return (0);
  }
  myArray.splice(0, 2);
  const newArray = myArray.sort((a, b) => b - a);
  return newArray[1];
}
console.log(secondLargest(process.argv));
