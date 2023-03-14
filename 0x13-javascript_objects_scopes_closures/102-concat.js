#!/usr/bin/node
// script that concats 2 files.First, second, third args as
// first source file, second source file and destination file respectively
const fs = require('fs');
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const outputPath = process.argv[4];

const file1Content = fs.readFileSync(file1Path, 'utf-8');
const file2Content = fs.readFileSync(file2Path, 'utf-8');
const outputContent = file1Content + file2Content;

fs.writeFileSync(outputPath, outputContent);
