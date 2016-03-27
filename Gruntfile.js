module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-mocha-test');

  grunt.initConfig({
    shell: {
      create_under_test_files: {
        command: '. ./scripts/create_under_test_js_files.sh'
      }
    },
    mochaTest: {
      test: {
        options: {
          reporter: 'spec'
        },
        src: ['optimizely_dev_tools/*/functions_test.unittests.js']
      }
    }
  });

  grunt.registerTask('test', ['shell:create_under_test_files', 'mochaTest']);
};
