#!/usr/bin/node
if (Math.floor(Number(process.argv[2])) === parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X'; // Concatenate 'X' to the row
    }
    console.log(row); // Print the completed row
  }
} else {
  console.log('Missing size');
}
