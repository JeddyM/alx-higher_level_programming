#!/usr/bin/node
// returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  const count = list.filter(value => value === searchElement);
  return count.length;
};
