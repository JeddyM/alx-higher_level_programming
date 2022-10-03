#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)){
        console.log('Missing size');
}
let indicator = '';
for (i = 0; i < num; i++)
{
	for (j = 0; j < num; j++) {
		indicator += 'x';
	}
	console.log(indicator);
	indicator = '';
}
