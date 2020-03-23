import looker_sdk

####### LOOKER MERGED QUERY SEARCH #######

# Instantiate SDK
sdk = looker_sdk.init31()

#Get A list of Dashboard Elements
looker_dashboard_elements = sdk.search_dashboards(fields='dashboard_elements')

dashbord_id_list = []
dashboard_count = 0

for dashboard in looker_dashboard_elements:
	for element in dashboard.dashboard_elements:
		if(element.merge_result_id is not None and element.dashboard_id not in dashbord_id_list):
			dashbord_id_list.append(element.dashboard_id)
			dashboard_count = dashboard_count + 1
print('There are ' + str(dashboard_count) + ' dashboards with merged queries.')
print(dashbord_id_list)