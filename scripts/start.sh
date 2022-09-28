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
&& echo "Running applications..." \
&& open /Applications/Loopback.app \
&& open traktor-pro/traktor-live-v2.tsi \
&& open ableton-live/traktor-live-v2\ Project/traktor-live-v2.als \
&& open audio-hijack/traktor-live-v2.ahsession \
&& echo "" \
&& echo "To complete the installation please do the following:" \
&& echo "" \
&& echo "1. Traktor Pro        - click: MASTER CLOCK START" \
&& echo "2. Traktor Pro        - click: MASTER CLOCK SYNC" \
&& echo "3. Ableton Live       - click: Options > External Sync (Ext button)" \
&& echo "4. Audio Hijack       - click: COMMAND + R (Record)" \
&& echo "5. Traktor Kontrol Z1 - push: MODE + A + B (MIDI mode)" \
&& echo "" \
&& echo "Enjoy!" \
&& echo ""
