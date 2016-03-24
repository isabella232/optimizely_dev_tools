def create_init_file(folder, example):
  filename = '__init__.py'
  f = open(folder + '/' + filename, 'w')
  f.write('# This file indicates this is a Python package. No modifications needed.')

def create_config_file(folder, example):
  filename = 'config.yaml'
  filecontent = ''
  if example:
    filecontent = '''- config_type: visitor_data_service
  master_label: XYZ Company
  help_text: Build audiences based on XYZ Company campaigns
  data_fetch_method: custom_javascript
  supported_fields:
    - name: campaigns
      display_name: XYZ Campaign
      help_text: Campaigns defined in the XYZ interface
      input_type: select
    - name: audience
      display_name: XYZ Audience
      help_text: Classifies web traffic by defined categories
      input_type: select
      values:
        - value: Education
          text: Education
        - value: Government
          text: Government
        - value: Hospitality
          text: Hospitality
        - value: Obscured
          text: Obscured
        - value: Residential
          text: Residential
        - value: SMB
          text: SMB
        - value: SOHO
          text: SOHO
        - value: Wireless
          text: Wireless
        - value: Enterprise Business
          text: Enterprise Business
        - value: Mid-Market Business
          text: Mid-Market Business'''
  else:
    filecontent = '''# When you create an audience integration, you can use this file
# to specify the fields that appear in the audience builder. 

#Example settings
- config_type: visitor_data_service
  master_label: # Use your company name, or the integration name
  help_text: # A helptext that will appear in the audience builder
  data_fetch_method: custom_javascript
  supported_fields:
    - name: # Unique identifier for condition
      display_name: # Unique human readable name for condition
      help_text: # A help text for the condition
      # Input type is select. It will creete a dropdown with the values specified below.
      input_type: select 
      values:
        - value: Education
          text: Education
        - value: Government
          text: Government
        - value: Hospitality
          text: Hospitality
        - value: Obscured
          text: Obscured
        - value: Residential
          text: Residential
    - name: # Unique identifier for condition
      display_name: # Unique human readable name for condition
      help_text: # A help text for the condition
      # Input type is select. It will create a dropdown with the values fetched with functions.py
      input_type: select
    - name: # Unique identifier for condition
      display_name: # Unique human readable name for condition
      help_text: # A help text for the condition
      # Input type is text. It will creete a textbox that the user can use to define a value.
      input_type: text
    - name: # Unique identifier for condition
      display_name: # Unique human readable name for condition
      help_text: # A help text for the condition
      # Input type is keyvalue. It will create two textboxes that the user can use to define a key and a value.
      input_type: keyvalue
      input_labels:
        - Key
        - Value

# Learn more regarding the options in this file on http://developers.optimizely.com'''   
  f = open(folder + '/' + filename, 'w')
  f.write(filecontent)

def create_integration_file(folder, default_config):
  file_name = 'integration.yaml'
  file_content = ''
  if default_config:
    with open('template_files/integration_yaml_default_template', 'r') as f:
      file_content = f.read()
      file_content = file_content.format(package_name=folder)
  else:
    with open('template_files/integration_yaml_unconfigured_template', 'r') as f:
      file_content = f.read()
      file_content = file_content.format(package_name=folder)
  with open(folder + '/' + file_name, 'w') as f:
    f.write(file_content)

def create_example_response_file(folder, example):
  filename = 'example.json'
  filecontent = '// Provide an example response from your streaming server (if you use dynamic audiences in your integration)'
  if example:
    filecontent = '''// Example response
 {"campaigns": [
  {
    "campaign": 51899,
    "seg_id": "1387680654",
    "timestamp": 1422302783,
    "categories": [
    {
     "categoryID": 17,
     "timestamp": 1422302778
    }
    ]
  },
  {
    "campaign": 51898,
    "seg_id": "1373691942",
    "timestamp": 1422302783,
    "categories": [
    {
     "categoryID": 17,
     "timestamp": 1422302778
    }
    ]
  },
  {
    "campaign": 48740,
    "seg_id": "828882042",
    "timestamp": 1422302783,
    "categories": [
    {
     "categoryID": 17,
     "timestamp": 1422302778
    }
    ]
  },
  {
    "campaign": 51898,
    "seg_id": "1373691942",
    "timestamp": 1422302783,
    "categories": [
    {
     "categoryID": 17,
     "timestamp": 1422302778
    }
    ]
  }
 ]}
'''
  f = open(folder + '/' + filename, 'w')
  f.write(filecontent)  

def create_functions_js_file(folder, example):
  filename = 'functions.js'
  filecontent = ''
  if example:
    filecontent = '''{
  fetchData: function() {
    $.getJSON("", function(data) {
      window["optimizely"] = window["optimizely"] || [];
      window["optimizely"].push(["storeThirdPartyData", "xyz", data]);
    });
  }
}
'''
  else:
    filecontent = '''{
  fetchData: function() {
    // If you use dynamic audiences, this function will be executed to fetch visitor data from a server.
    // Example:

    /**
     * $.getJSON("url", function(data) {
     *  window["optimizely"].push(["storeThirdPartyData", "xyz", data]);
     * });
     */
  }
}
  '''
  f = open(folder + '/' + filename, 'w')
  f.write(filecontent) 

def create_functions_py_file(folder, example):
  filename = 'functions.py'
  filecontent = ''
  if example:
    filecontent = '''
import requests

from optimizely_platform import exceptions
from optimizely_platform import objects
def get_dynamic_audience_conditions(integration_settings):
  url = str(integration_settings['url'])

  response = requests.get(url).json()

  audience_condition_options = []

  try:
    for campaign in response:
      audience_condition_options.append(
          objects.AudienceConditionOption(campaign['campaignId'], campaign['name'].strip()))

    return [objects.AudienceCondition('campaigns', audience_condition_options)]
  except Exception as e:
    raise e''' 
  else:
    filecontent = '''# This file allows you to define the logic to fetch dynamic audiences
#
# from optimizely_platform import exceptions
# from optimizely_platform import objects
# def get_dynamic_audience_conditions(integration_settings):
#   url = str(integration_settings['url'])

#   response = requests.get(url).json()

#   audience_condition_options = []

#   try:
#     for campaign in response:
#       audience_condition_options.append(
#           objects.AudienceConditionOption(campaign['campaignId'], campaign['name'].strip()))

#     return [objects.AudienceCondition('campaigns', audience_condition_options)]
#   except Exception as e:
#     raise e''' 
  f = open(folder + '/' + filename, 'w')
  f.write(filecontent)   


