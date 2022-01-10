import time
import datetime

while(1):
    now = datetime.datetime.now()
    time.sleep(1)
    if now.minute == 0 and now.second == 0:
        print("뻐꾹! 현재시간은 {} 입니다.".format(now))
    else:
        print(now)