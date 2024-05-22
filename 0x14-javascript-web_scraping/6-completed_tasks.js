#!/usr/bin/node
const request = require('request');
const url = process.argv[2];


let users_dic = {};
request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const data = JSON.parse(body);

        for (let i = 0; i < data.length; i++) {
            if (!(data[i].userId in users_dic)) {
                users_dic[data[i].userId] = 0;
            }
        }
        
        for (const id in users_dic)   {
             /* console.log(id); */
            
            for (let j = 0; j < data.length; j++) {
                if (data[j].completed === true && data[j].userId === parseInt(id)) {
                    users_dic[data[j].userId] += 1;
                }
            }
            
        }
        console.log(users_dic);
}    
}
)

