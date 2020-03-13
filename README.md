Weak Person Feed

## Running
Run two processes:
1. ```python3 main.py```
2. ```./sync.sh```

## Requirements
- Intended to run on osx or linux (including rapsberry pi)
- Intended to work with any video capture device, including built-in webcams, external webcams, and capture enabled cameras
- Requires python 3 with open cv 2 installed (`pip3 install cv2`)
- Requires aws cli (see s3 configuration section)

## S3 Configuration
You need to configure the aws cli to use an aws account: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
- Edit `sync.sh` to use your own profile / bucket
