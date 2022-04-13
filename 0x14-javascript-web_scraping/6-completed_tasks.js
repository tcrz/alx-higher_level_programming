#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const cmpTasks = {};
    tasks.forEach(n => {
      if (n.completed) {
        cmpTasks[n.userId] = 0;
      }
    });
    Object.keys(cmpTasks).forEach(x => {
      tasks.forEach(n => {
        if (n.userId === parseInt(x) && n.completed) {
          cmpTasks[n.userId] += 1;
        }
      });
    });
    console.log(cmpTasks);
  }
});
