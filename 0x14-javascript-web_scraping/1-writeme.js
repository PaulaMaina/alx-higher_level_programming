#!/usr/bin/node
const filesys = require('fs');
const fileName = process.argv[2];
const input = process.argv[3];

filesys.writeFile(fileName, input, 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
    }
  });
