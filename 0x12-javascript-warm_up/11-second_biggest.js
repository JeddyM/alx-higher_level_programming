#!/usr/bin/node

function second_largest (myArray) {
	if (myArray.length === 2 || myArray.length === 3) { 
		return (0);
	}
	myArray.splice(0, 2)
	let newArray = myArray.sort((a, b) => b - a);
	return newArray[1];
}
console.log(second_largest([2,3,6,7]));
console.log(second_largest(process.argv));
