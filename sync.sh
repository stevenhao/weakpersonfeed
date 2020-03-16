echo Syncing every 10 seconds...
while :; do
  echo Syncing... $(date)
  aws --profile sven s3 sync out s3://weakpersonfeed/
  find out -type f -mtime +1 | xargs rm
  sleep 10
done
