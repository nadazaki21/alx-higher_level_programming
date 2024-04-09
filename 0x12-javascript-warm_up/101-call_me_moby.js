#!/usr/bin/node

module.exports = function(x, theFunction) {
    for (let i = 0; i < x; i++) {
      // Call the function with no arguments, as required by the main file
      theFunction();
    }
  };