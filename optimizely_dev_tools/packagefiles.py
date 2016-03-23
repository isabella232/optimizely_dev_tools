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

def create_integration_file(folder, example):
  filename = 'integration.yaml'
  filecontent = ''
  if example:
    filecontent = '''xyz:
  addon_type: integration
  beta: false
  categories:
  - Audiences
  channels:
  - web
  products:
  - ab_testing
  - personalization
  description: Use this integration to create Optimizely
    audiences based on visitor data from XYZ.  This
    integration requires an existing account with XYZ.
  developer: XYZ
  developer_website: null
  enabled: true
  logo_file_name: logo.png
  master_label: XYZ
  partner_dir_url: https://www.optimizely.com/partners/technology/XYZ
  permission_required: xyz_integration
  settings_metadata:
    fields:
    - inputType: text
      label: Streaming URL
      name: streaming_url
      required: true
      includeInSnippet: true
      saveLocations:
      - project
    - inputType: text
      label: Campaigns URL
      name: campaigns_url
      required: true
      saveLocations:
      - project    
    generalHelp:
      project:
        kbLink: https://help.xyz.com/optimizely-integration
    onOffableAtExperimentLevel: false
    onOffableAtProjectLevel: true
    settingsHelp: {}'''
  else:
    filecontent = folder + ''':
  addon_type: # Value: integration or app
  beta: false
  categories:
  - # Fill in the categorie type displayed on the integrations tab. Values: Analytics, Call tracking, Audiences, Heatmap, Content Management, Productivity
  channels:
  - web
  products:
  - ab_testing
  - personalization
  description: # Provide a description of what your app does. The description will be displayed on the integration tab.
  developer: # The name of you or your company
  developer_website: # Your website
  enabled: true
  logo_file_name: # What is the filename of your logo (in the assets folder)
  master_label: # Name of the integration as displayed on the integrations tab
  partner_dir_url: https://www.optimizely.com/partners/technology/'''+ folder+'''
  permission_required: '''+folder+'''_integration
  settings_metadata: # Define setting fields that are referenceable in all of your integration logic. Example:
  # fields:
  # - inputType: text
  #   label: Streaming URL
  #   name: streaming_url
  #   required: true
  #   includeInSnippet: true
  #   saveLocations:
  #   - project
  # - inputType: text
  #   label: Campaigns URL
  #   name: campaigns_url
  #   required: true
  #   saveLocations:
  #   - project 
    generalHelp:
      project:
        kbLink: # Link to a help article regarding the integration
    onOffableAtExperimentLevel: false
    onOffableAtProjectLevel: # Does this integration have an on/off switch or is it only a integrations tab listing?
    settingsHelp: {}'''



  f = open(folder + '/' + filename, 'w')
  f.write(filecontent)  

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
};
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
};
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


