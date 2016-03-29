module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-mocha-test');
  grunt.initConfig({
    shell: {
      create_under_test_files: {
        // pass path as an argument
        command: './scripts/create_under_test_js_files.sh ' + grunt.option('path')
      }
    },
    mochaTest: {
      test: {
        options: {
          reporter: 'spec'
        },
        src: [grunt.option('path') + '/functions_test.unittests.js']
      }
    }
  });
  
  grunt.registerTask('test', ['shell:create_under_test_files', 'mochaTest']);
};
