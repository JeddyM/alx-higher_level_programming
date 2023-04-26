#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('Error: ', error);
  } else {
    console.log('Code: ', response.statusCode);
  }
});
