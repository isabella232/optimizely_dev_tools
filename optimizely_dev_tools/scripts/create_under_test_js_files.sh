#!/usr/bin/env sh

# This script creates a modified version of every functions.js file, named functions.under_test.js, with
# "module.exports = " prepended to the original file. Assigning the functions mapping to the
# "module.exports = " variable accommodates testing of the functions.
echo $1
find $1 -name functions.js | grep -o '.*/' | while read functions_js_file_dir; do
  original_file_name="functions.js"
  under_test_file_name="functions.under_test.js"
  echo 'module.exports = ' | cat - $functions_js_file_dir$original_file_name > $functions_js_file_dir$under_test_file_name
done
