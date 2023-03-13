#!/usr/bin/node
// parse the first arg as an int
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = ''; // inner loop initialize an empty string
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
