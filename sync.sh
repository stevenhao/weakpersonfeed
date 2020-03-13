echo Syncing every 10 seconds...
while :; do
  echo Syncing... $(date)
  aws --profile sven s3 sync out s3://weakpersonfeed/
  sleep 10
done
