import looker_sdk
import csv
import datetime

########################################################################################
#This script exports query info about all vizs in all dashboard (repository documenter)#
########################################################################################

sdk = looker_sdk.init31()

# Generate all dashboard data
all_dashboard_data = sdk.all_dashboards()

# Save all dashboard ids to a list
dashboard_id_list = []
dashboard_query_info_list = []
for dashboard in all_dashboard_data:
	dashboard_id_list.append(dashboard.id)

# Get query info from each dashboard	
for dashboard_id in dashboard_id_list:
	dashboard_data = sdk.dashboard(dashboard_id)
	
	if not dashboard_data.deleted:
		for i in range(len(dashboard_data.dashboard_elements)):
			if dashboard_data.dashboard_elements[i].query is not None:
				#Create list of query info
				dashboard_query_info_list.append([dashboard_data.title,dashboard_data.dashboard_elements[i].title,dashboard_data.dashboard_elements[i].query.id,dashboard_data.dashboard_elements[i].query.model,dashboard_data.dashboard_elements[i].query.view,dashboard_data.dashboard_elements[i].query.fields])

# Export to csv	
now = datetime.datetime.now()				
with open("S:\EIS\Looker\API\Repository Documenter\Looker_Queries_" + now.strftime("%Y%m%d") + ".csv", "w", newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['Dashboard Title','Vis Title','Query ID','Model','View','Fields'])
	writer.writerows(dashboard_query_info_list)