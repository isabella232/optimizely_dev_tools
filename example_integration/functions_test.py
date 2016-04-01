import mock

import unittest

from optimizely_platform import exceptions
from optimizely_platform import objects

import functions


class FunctionsTest(unittest.TestCase):

  def test_get_dynamic_audience_conditions__successful_fetch(self):
    SAMPLE_APP_SETTINGS = {
          'account_id': 83043022
      }

    MOCK_RESPONSE_OBJECT = mock.Mock()
    MOCK_RESPONSE_OBJECT.status_code = 200
    MOCK_RESPONSE_OBJECT.json.return_value = {
      "campaigns": [{
          "name": "Age: 20-30",
          "identifier": "age_20_30"
      }, {
          "name": "Buying:scooter",
          "identifier": "buying_scooters"
      }, {
          "name": "Browser:chrome",
          "identifier": "browser_chrome"
      }]
  }
    EXPECTED_AUDIENCE_CONDITIONS = [objects.AudienceCondition('Sample Condition', 
          [objects.AudienceConditionOption('age_20_30', 'Age: 20-30'), 
           objects.AudienceConditionOption('buying_scooters', 'Buying:scooter'), 
           objects.AudienceConditionOption('browser_chrome', 'Browser:chrome')])]


    with mock.patch('requests.get', return_value = MOCK_RESPONSE_OBJECT) as mock_requests_get:
        audience_conditions = functions.get_dynamic_audience_conditions(SAMPLE_APP_SETTINGS)

    self.assertItemsEqual(EXPECTED_AUDIENCE_CONDITIONS, audience_conditions)

    mock_requests_get.assert_called_once_with('https://integrations.optimizely.how/api/83043022/campaigns.json')

