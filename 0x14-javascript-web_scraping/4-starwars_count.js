#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
let num = 0;

req.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
