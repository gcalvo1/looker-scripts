# looker-scripts

<h3> <strong> Merged Query Search </strong> </h3>
<p>
Python script that prints the number, and the ids, of dashboards containing merged queries
</p>
<h3> <strong> Repository Documenter </strong> </h3>
Python script that exports query info about visualizations in all dashboards into a .csv file. Documented fields include:
<ul>
	<li>Dashboard Title</li>
	<li>Vis Title</li>
	<li>Query ID</li>
	<li>Model</li>
	<li>View</li>
	<li>Fields</li>
</ul>
<h3> <strong> Secure User Spaces </strong> </h3>
<p>
Python script that identifies Looker users whose user space is not secure. By default, a new Looker user's personal space is public to all users. This script will make those spaces private.
</p>

<h3> <strong> User Downgrade </strong> </h3>
<p>
Python script that identifies two types of users:
<ol>
	<li> User that has not logged into Looker in one year </li>
	<li> User with standard features (Explore/SQL Runner) that has not used the features in three months </li>
</ol>

and emails them a notification warning of a downgrade or whatever type of messaging you would like.

*This script uses a MySQL Looker application database to identify and log users. That can be replaced by the Looker API or another database based on your use case and Looker setup. Obviously, the date checks in the script can be modified to meet your use case.
</p>
