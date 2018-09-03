import time

while True:
    time.sleep(1)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "  hello world")
