import sys

counter = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write("%s:%s" % (counter, line))
    counter += 1
    sys.stdout.flush()
