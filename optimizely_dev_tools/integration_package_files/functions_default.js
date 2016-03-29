{
  fetchData: function() {
    $.getJSON("", function(data) {
      window["optimizely"] = window["optimizely"] || [];
      window["optimizely"].push(["storeThirdPartyData", "xyz", data]);
    });
  }
}
