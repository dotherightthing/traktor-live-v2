#!/bin/bash
#
# File: ./scripts/install.sh
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

# install project files
cd $INIT_CWD \
&& echo "Installing ClyphX Pro configuration" \
&& rm -rf ~/NativeKONTROL/ClyphX_Pro \
&& rm -rf '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions' \
&& cp -R 'clyphx-pro/ClyphX_Pro' ~/NativeKONTROL \
&& cp 'clyphx-pro/user_actions/' '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/' \
&& echo "Installing Loopback configuration" \
&& cp 'loopback/Devices.plist' ~/Library/Application\ Support/Loopback \
&& open traktor-pro/push2-traktor-live.tsi \
&& open ableton-live/push2-traktor-live Project/push2-traktor-live.als \
&& open audio-hijack/push2-traktor-live.ahsession \
&& echo "Installation complete"
