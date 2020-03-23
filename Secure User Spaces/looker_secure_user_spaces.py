import looker_sdk

##################################################################################
#This script removes "view" access from the "All Users" group in all user spaces #
##################################################################################

sdk = looker_sdk.init31()

#Generate all space data for spaces that have the User space as the parent (User space id = 2)
user_space_data = sdk.search_spaces(parent_id = 2)

print("Found " + str(len(user_space_data)) + " user spaces")

#Loop through the array of user spaces
for user_space in user_space_data:
	#Generate content access data for the user space
	content_access_data = sdk.all_content_metadata_accesses(content_metadata_id = user_space.content_metadata_id)	
	
	#Loop through the array of access groups
	for conent_access in content_access_data:
		#Only remove the access for the "All Users" group (id = 1)
		if conent_access.group_id == 1 and (conent_access.permission_type == "view" or conent_access.permission_type == "edit"):
		
			#Set up parameters for delete_content_metadata_access
			id = conent_access.id

			#run delete_content_metadata_access
			deleted_content_access = sdk.delete_content_metadata_access(id)
			
			print(user_space.name + "'s user space set to private")