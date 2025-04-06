### Backup:
A backup is basically a copy of your important data, stored safely somewhere else, so that if something happens due to which the original daat is lost, we can get it back.

Backups are needed:
1. Sometimes, hardware can fail.
2. Some cyberattack may result in lossing your data.
3. Data can be deleted by mistake 

We can group AWS backups as:<br>
1. Service-specific backups (like EBS, RDS, DynamoDB)
2. Centralized backup with AWS Backup

#### AWS Backup:
AWS backup is a fully managed service by AWS that helps you automate, organize, and monitor backups for all-resources.
It has centralized Control and supports many services like:
> EBS volumes (like hard drives for EC2)<br>
> RDS databases<br>
> EFS file systems, etc.<br>

### EBS backup:
#### 1. Manual Backup:
##### Take Backup:<br>
Go to the EBS volume and then go to actions, and choose "Create Snapshot". Now, add description for the snapshot and create snapshot.

##### Recovery from Backup:<br>
Go to snapshots. Now, choose the snapshot that we took, then select actions and choose create volume from snapshot. The volume should be greater than size of snapshot. And, click on create volume. Now, this volume can be attched to EC2 instances. As, the data is backedup.

#### 2. Automated Backup:
##### Take Backup:<br>
Go to Lifecycle manager, choose target resource type as volume. Now, choose the target resource tags. Add, policy description and let IAM role to be default, and ebale policy status.
Now, configure schedule according to our need when the snapshot should be taken. Finally, review policy and create policy.
Now, it can be seen in snapshots that the snapshots of EBS volume are taken according to the schedule we added.

##### Recovery from Backup:<br>
It follows the same steps that we covered in manual backup 

### EFS Backup:
#### 1. Manual Backup:
##### Take Backup:
Go to AWS Backup service. Click on Create Backup Plan → choose Build a new plan.
Add backup rule. Under Resource Assignments, give the assignment name and choose EFS as the resource type.
Select the EFS file system you want to back up and click Assign resources.
Now, AWS will take a backup of the selected EFS file system.

##### Recovery from Backup:
Go to AWS Backup → Backup vaults → select the vault where the EFS backup is stored. Click on the backup, then select Restore.
Enter a name for the new EFS file system and choose options as per your need. Click Restore backup.
Now, this will create a new EFS file system with all data recovered.

#### 2. Automated Backup:
##### Take Backup:
Go to AWS Backup and create a Backup Plan and choose Start with a template or Build a new plan.
Set backup frequency (hourly, daily, weekly, etc.). Then, in Resource Assignments, assign EFS file systems by selecting the appropriate resource type and EFS ARNs or tags. Now, backups of EFS will be taken automatically based on this schedule.

##### Recovery from Backup:
Go to the Backup vault, choose the EFS backup you want to restore. Click on Restore, then configure EFS optionsand launch the restored file system.
Mount this restored EFS file system to EC2 instances just like the original one.

### RDS Backup:<br>
#### 1. Manual Backup:
##### Take Backup:<br>
Go to RDS Dashboard → Select the RDS instance you want to back up. Click on Actions → choose Take snapshot. Give the snapshot a name and click Take Snapshot.<br>
AWS will now create a snapshot of the RDS instance.

##### Recovery from Backup:
Go to Snapshots in the RDS console → choose the snapshot you want to restore. Click Actions → Restore Snapshot. Provide a new DB instance identifier, choose instance type, storage, VPC, etc. Click Restore DB Instance. Once restored, this creates a new RDS instance with the data from the snapshot.

#### 2. Automated Backup:
##### Take Backup:
Go to RDS Dashboard → Select your RDS instance. Click Modify, scroll to the Backup section.
Enable Automated Backups by setting the backup retention period (e.g., 7 days). Choose the preferred backup window (when automated backups should occur). Click Continue and then Apply Immediately (or during the next maintenance window). Now, RDS will automatically take backups.

##### Recovery from Backup:
Go to RDS → Databases → click Create database → select Restore from backup. You can restore from the latest automatic backup or point-in-time within the retention period. Choose DB instance configurations and click Restore. A new instance will be created with the data as it was at that specific time.