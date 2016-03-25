#!/usr/bin/env node

(function() {
  var fs = require('fs');
  var functions_js = fs.readFileSync(process.argv[2], {encoding: 'utf8'});
  
  // can't get line number with try/catch so letting eval throw exception directly
  var result = eval('funcJs = ' + functions_js);
  if (!("fetchData" in result)) {
    throw "fetchData not defined in functions.js";
  } 
})();
