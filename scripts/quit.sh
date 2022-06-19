#!/bin/bash
#
# File: ./scripts/close.sh
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
&& echo "Closing applications..." \
&& osascript -e 'quit app "Loopback.app"' \
&& osascript -e 'quit app "Traktor.app"' \
&& osascript -e 'quit app "Ableton Live 10 Standard.app"' \
&& osascript -e 'quit app "Audio Hijack.app"' \
&& open ~/Websites/push2-traktor-live/_admin/Recordings\ from\ Audio\ Hijack \
&& echo "Goodnight!" \
&& echo ""
