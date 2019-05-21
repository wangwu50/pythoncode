import sched
import time
from datetime import datetime

# 使用原生sched实现
schedule = sched.scheduler(time.time, time.sleep)


def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))


if __name__ == '__main__':
    schedule.enter(0, 0, printTime, (10,))
    schedule.run()

