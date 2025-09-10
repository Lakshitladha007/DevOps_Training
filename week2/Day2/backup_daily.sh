#!/bin/bash
 
SOURCE="/home"
DEST="/backup"
FILENAME=$(date +"%Y-%m-%d")
 
tar -czf $DEST/home_backup_$FILENAME.tar.gz $SOURCE
 
echo "Backup completed at $FILENAME" >> /var/log/backup.log