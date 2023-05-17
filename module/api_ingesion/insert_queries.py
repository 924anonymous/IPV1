# """
# Purpose : input parameters for queryGenerator function
# """

api_configuration_details_query = '''
/************************ API CONFIGURATION DETAILS ************************/
insert into config.api_configuration_details (
API_TYPE,
API_NAME,
API_URL) VALUES ('{api_type}','{api_name}','{api_url}');'''
