var devTools = require('optimizely-dev-tools-npm');

module.exports = function(grunt) {
  
  grunt.registerTask('test', function () {
    devTools.setupTestingInfrastructure(grunt.option('path'));
  });
};
