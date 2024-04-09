#!/usr/bin/node

const { readFile, writeFile } = require('fs');
readFile(process.argv[2], 'utf8', (err, fileA) => {
  if (err) throw err;
  readFile(process.argv[3], 'utf8', (err, fileB) => {
    if (err) throw err;
    writeFile(process.argv[4], fileA + fileB, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
