import time
import datetime
i = datetime.datetime.now()
print(i)
time.sleep(10)
ii = datetime.datetime.now()
print(str(ii - i).split(".")[0])