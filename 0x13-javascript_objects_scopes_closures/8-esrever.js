#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(element => {
    newList.unshift(element);
  });
  return newList;
};
