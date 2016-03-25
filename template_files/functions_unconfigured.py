# This file allows you to define the logic to fetch dynamic audiences
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
#     raise e
