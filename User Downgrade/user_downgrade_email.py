import sys
import looker_sdk
import datetime
import mysql.connector
import notifications
import email_body

####### LOOKER USER DOWNGRADE EMAIL #######
# If a user has explore access and has not used the features in three months, 
# send an email that the user will be downgraded to viewer
# If a users has not logged-in in a year, send an email that the user will be disabled

### FILE DETAILS ##
#notifications.py is a file with a function that sends an email. File not included for credential privacy
#email_body.py is a file with the body to the emails. File not included as its personal to the developer

#Query to get list of standard users that have explored or used sql runner in the last 3 months
#Unioned with a list of users that received the downgrade warning email in the last 3 months
#**Developer's choice as to where to get this info from. MySQL db can be used or Looker API. 
#**Removed MySQL connection info and query

mycursor.execute('SELECT DISTINCT user_id FROM standard_user_warning_suppression_list_vw')

myresult = mycursor.fetchall()

standard_users_with_usage_list = []
for user_id in myresult:
  standard_users_with_usage_list.append(user_id[0])

# Instantiate SDK
sdk = looker_sdk.init31()

#Get A list of Users with Attributes    
looker_users = sdk.all_users()

today_for_db = datetime.date.today().strftime("%Y-%m-%d")
datetime_one_year_ago = datetime.date.today() - datetime.timedelta(days=365)

for user in looker_users:
    if(user.credentials_saml is not None and not(user.is_disabled)): 
        #Has not logged-in in a year        
        if(datetime.datetime.strptime(user.credentials_saml.logged_in_at.replace('Z', '').replace('T',' '), '%Y-%m-%d %H:%M:%S.%f').date() == datetime_one_year_ago ):
            #Email User with account disable warning
            email_subject = "Looker Account Disable Warning - " + user.email
            disable_email_body = email_body.disable_body_html(user.email)
            notifications.send_email("sender_email@domain.com", [user.email], ["cc_email@domain.com"], [], email_subject, disable_email_body)

            #Insert warning into log table
            mycursor = mydb.cursor()
            sql = "INSERT INTO user_downgrade_log VALUES (%s, %s, %s, %s)"
            val = (user.id, user.email, "Disable", today_for_db)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Disable Log Record Inserted - " + user.email)

        else:
            #Email standard users without usage in last 3 months
            for group_id in user.group_ids:
                if(group_id) in [YOUR STANDARD GROUP IDS] and user.id not in standard_users_with_usage_list: #need to check db to make sure user did not get the email already
                    #Email User with account downgrade warning
                    #Need to save these users to a db to ensure they only get the email once    
                    email_subject = "Looker Account Downgrade Warning - " + user.email
                    downgrade_email_body = email_body.downgrade_body_html(user.email)
                    notifications.send_email("sender_email@domain.com", [user.email], ["cc_email@domain.com"], [], email_subject, downgrade_email_body)

                    #Insert warning into log table
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO user_downgrade_log VALUES (%s, %s, %s, %s)"
                    val = (user.id, user.email, "Downgrade", today_for_db)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Downgrade Log Record Inserted - " + user.email)         


