#!/usr/bin/python
import sys
try:
    file(sys.argv[1]).read(int(sys.argv[2]))
except IOError, e:
    print >>sys.stderr, "%s: %s" % (sys.argv[1], e.strerror)
    sys.exit(e.errno)
print "%s: Success" % (sys.argv[1])
sys.exit(0)
