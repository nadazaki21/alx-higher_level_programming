#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i = 2;
  while (!(process.argv[i] === undefined)) {
    const target = parseInt(process.argv[i]);
    let biggerThan = 0;
    let j = 2;
    while (!(process.argv[j] === undefined)) {
      if (target < parseInt(process.argv[j])) {
        biggerThan++;
      }
      j++;
    }
    if (biggerThan === 1) {
      console.log(process.argv[i]);
      break;
    }
    i++;
  }
}
