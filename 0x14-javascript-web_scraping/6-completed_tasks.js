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
    let userIdList = [];
    const tasks = JSON.parse(body);
    tasks.forEach(n => userIdList.push(n.userId));
    userIdList = [...new Set(userIdList)];
    const cmpTasks = {};
    userIdList.forEach(n => {
      cmpTasks[n] = 0;
    });
    userIdList.forEach(x => {
      tasks.forEach(n => {
        if (n.userId === x && n.completed) {
          cmpTasks[n.userId] += 1;
        }
      });
    });
    console.log(cmpTasks);
  }
});
