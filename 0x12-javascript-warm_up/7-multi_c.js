#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)){
        console.log('Missing number of occurrences')
}
for (i = 0; i < num; i++)
{
	console.log('C is fun')
}
