#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const usersDic = {};
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    for (let i = 0; i < data.length; i++) {
      if (!(data[i].userId in usersDic)) {
        usersDic[data[i].userId] = 0;
      }
    }

    for (const id in usersDic) {
      /* console.log(id); */

      for (let j = 0; j < data.length; j++) {
        if (data[j].completed === true && data[j].userId === parseInt(id)) {
          usersDic[data[j].userId] += 1;
        }
      }
    }
    console.log(usersDic);
  }
}
);
