// TODO: Turn this into a tiny npm module?

module.exports = {
  mockWindowObject: function() {
    global.window = {};
    window.optimizely = [];
    window.location = {};
    global.localStorage = {};
    window.setTimeout = function(func, timeout) {
      func();
    };
  }
};
