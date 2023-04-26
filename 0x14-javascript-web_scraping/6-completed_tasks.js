#!/usr/bin/node

/*
A script that computes the number of tasks completed by user id.

  The first argument is the API URL:
    `https://jsonplaceholder.typicode.com/todos`
  Only print users with completed task
  You must use the module request
*/

const request = require('request');
const requestURL = process.argv[2];

request.get(requestURL, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const todosList = JSON.parse(body);
  // filter to obtain a list of all completed todos
  const completedTodos = todosList.filter(todo => todo.completed === true);
  const userCompletedTodos = {}; // dict in form of {'userId': sum of completed todos}
  completedTodos.forEach(todo => {
    if (!userCompletedTodos[todo.userId]) {
      userCompletedTodos[todo.userId] = 1;
    } else {
      userCompletedTodos[todo.userId] += 1;
    }
  });
  console.log(userCompletedTodos);
});
