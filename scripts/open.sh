#!/bin/bash
#
# File: ./scripts/open.sh
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
&& echo "Running applications" \
&& open /Applications/Loopback.app \
&& open traktor-pro/push2-traktor-live.tsi \
&& open ableton-live/push2-traktor-live\ Project/push2-traktor-live.als \
&& open audio-hijack/push2-traktor-live.ahsession \
&& echo "----------8<----------" \
&& echo "Traktor Pro - please click: MASTER CLOCK START" \
&& echo "Ableton Live - please click: Options > External Sync" \
&& echo "Audio Hijack - please click: COMMAND+R" \
&& echo "---------->8----------"
