import cv2
import datetime
import time
from pathlib import Path
cap = cv2.VideoCapture(0)
startTime = time.ctime()
capture_id = "test_capture"

def secs():
    return time.time()

start_time = secs()
for i in range(100):
    ret, frame = cap.read()
    now = datetime.datetime.now()
    delay = start_time + i - secs()
    if delay > 0:
        time.sleep(delay)
    now = datetime.datetime.now()
    root_dir = "out/%s" % capture_id
    cur_dir = root_dir + "/" + now.strftime("%m/%d/%H/%M");
    Path(cur_dir).mkdir(parents=True, exist_ok=True)
    cur_file = now.strftime("%S.jpg")
    path = cur_dir + "/" + cur_file
    print(path)
    try:
        cv2.imwrite(path, frame)     # save frame as JPEG file
    except:
        print("error on", path)
