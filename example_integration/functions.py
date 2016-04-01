import requests

from optimizely_platform import exceptions
from optimizely_platform import objects


def get_dynamic_audience_conditions(integration_settings):
  
  AUDIENCE_OPTIONS_ENDPOINT = (
    'https://integrations.optimizely.how/api/{0}/campaigns.json')

  account_id = integration_settings['account_id']

  request_url = AUDIENCE_OPTIONS_ENDPOINT.format(account_id) 
  
  response = requests.get(request_url).json() 

  # Build list of audience conditions
  audience_condition_options = []

  try:
    for campaign in response['campaigns']:
      condition = objects.AudienceConditionOption(campaign['identifier'], campaign['name'].strip())
      audience_condition_options.append(condition)

    return [objects.AudienceCondition('Sample Condition', audience_condition_options)] 
  
  except:
    raise

def validate_integration_settings(integration_settings):
  try:
    verify_account(integration_settings['account_id'])
  except:
    raise optimizely_platform.exceptions.IntegrationSettingsValidationError(
        'Your Account ID appears to be invalid.')

  return optimizely_platform.Configuration.get_integration_strings()

# Verify a User's Account Id
def verify_account(account_id):
  VERIFY_ACCOUNT_ENDPOINT = 'https://api.sample-app.com/verify/'

  return requests.get(VERIFY_ACCOUNT_ENDPOINT + account_id).json()
