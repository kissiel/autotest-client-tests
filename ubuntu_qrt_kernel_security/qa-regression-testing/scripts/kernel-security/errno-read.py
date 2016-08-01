#!/usr/bin/env python
import sys
try:
    file(sys.argv[1]).read(int(sys.argv[2]))
except IOError as e:
    print("%s: %s" % (sys.argv[1], e.strerror), file=sys.stderr)
    sys.exit(e.errno)
print("%s: Success" % (sys.argv[1]))
sys.exit(0)
