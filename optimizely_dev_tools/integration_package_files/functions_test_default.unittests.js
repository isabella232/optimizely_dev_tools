var expect = require('optimizely-dev-tools-npm/node_modules/expect.js');
var integrationFunctions = require('./functions.under_test');
var devTools = require('optimizely-dev-tools-npm');

describe('my integration functions', function(){

  describe('#fetchData', function(){

    beforeEach(function() {
      devTools.mockWindowObject();
    });

    it('should coerce the visitor data into the expected format and store it via storeThirdPartyData', function() {

      // this is just an illustrative `fetchData` function
      var exampleFetchData = function() {
        var data = {'campaigns': []};
        if (window['integration_data_object'] && window['integration_data_object'].hasOwnProperty('campaigns')) {
          var campaigns = window['integration_data_object']['campaigns'];
          for (var i=0, numCampaigns=campaigns.length; i<numCampaigns; i++) {
            if (campaigns[i]['campaign']) {
              data['campaigns'].push(campaigns[i]['campaign']);
            }
          }
          window['optimizely'].push(['storeThirdPartyData', 'my_integration', data]);
        }
      };

      window['integration_data_object'] = {'campaigns': [{'campaign': 51899,
                                                          'timestamp': 1422302783,
                                                         },
                                                         {'campaign': 48740,
                                                          'timestamp': 1422302783,
                                                         }]};

      // when you're writing the real tests, delete `exampleFetchData` above and invoke your real `fetchData` function
      // here as `integrationFunctions.fetchData()`.
      exampleFetchData();

      expect(window['optimizely']).to.eql(
          [['storeThirdPartyData', 'my_integration', {'campaigns': [51899, 48740]}]]);
    });

  });

});
