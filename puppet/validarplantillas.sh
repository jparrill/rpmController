find . -type f -size +0 -name *.erb |xargs /usr/bin/erb -P -x -T '-' | /usr/bin/ruby -c
