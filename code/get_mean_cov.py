import sys

vals = []
for l in sys.stdin:
    vals.append(int(l.strip().split()[-1]))

print(sum(vals)/len(vals))
