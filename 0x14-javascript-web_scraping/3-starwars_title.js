#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
