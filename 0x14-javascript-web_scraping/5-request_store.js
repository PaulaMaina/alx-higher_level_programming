#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

req.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
