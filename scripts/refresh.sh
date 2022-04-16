#!/bin/bash
#
# File: ./scripts/refresh.sh
#
# Note:
# chmod a+x = Change access permissions of this file, to 'e[x]ecutable' for '[a]ll users'
#
# Example:
# ---
# chmod a+x scripts/*sh
# ---

# e: exit the script if any statement returns a non-true return value
# v: print shell input lines as they are read (including all comments!)
set -e

# open files to run apps
cd $INIT_CWD \
&& open ableton-live/push2-traktor-live\ Project/push2-traktor-live.als \
&& echo ""
