"""
Class: MidiFighterTwister
_________________________________________________________________________________________

TESTING:

```sh
# note: the version string will change if Live auto-updates itself
tail -f '/Users/dan/Library/Preferences/Ableton/Live 10.1.43/Log.txt'
```

```py
self.canonical_parent.log_message('Hello world')
```
_________________________________________________________________________________________

"""

# Import UserActionsBase to extend it.
from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# import datetime

# Your class must extend UserActionsBase.
class MidiFighterTwister(UserActionsBase):
	# Your class must implement this method.
	def create_actions(self):
		# called by Macros.txt
		self.add_clip_action('reset_mapped_track_controls', self.reset_mapped_track_controls)
		self.add_clip_action('slice_track_clip_to_quarters', self.slice_track_clip_to_quarters)

	# reset mapped controls on provided track name
	def reset_mapped_track_controls(self, action_def, args):
		track_name = args.upper()
		action_list = ''
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P1 127;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P2 63;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P3 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P4 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P5 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P6 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P7 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P8 63;'
		action_list += 'WAIT 1;'
		action_list += 'MSG "Reset ' + track_name + '";'
		action_list += 'PUSH MSG "Reset ' + track_name + '"'

		self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

	# slice selected clip on provided track name into 4 parts
	# https://www.youtube.com/watch?v=rjSTTO3f4_Y
	# TODD automate switching Push2 into Note mode to see slices and do sequencing
	# TODO check Gain amt - seems hotter than sample track when flattening
	# TODO put all the slices into the sequencer automatically
	def slice_track_clip_to_quarters(self, action_def, args):
		track_name = args.upper()
		action_list = ''
		action_list += '"' + track_name + ' SLICED"/DEL;'
		action_list += '"' + track_name + '"/CLIP(SEL) TOSIMP;'
		action_list += 'WAIT 5;'
		action_list += 'SEL/NAME "' + track_name + ' SLICED";'
		action_list += 'SEL/DEV SIMP PLAYMODE SLICE;'
		action_list += 'SEL/DEV SIMP SMODE BEAT;'
		action_list += 'SEL/DEV SIMP MULT 8;'
		action_list += 'SEL/DEV SIMP GAIN 108;'
		action_list += 'ADDCLIP SEL 1;'
		action_list += 'SEL "' + track_name + ' SLICED";'
		action_list += 'SEL/CLIP NAME "SLICED";'
		action_list += '"' + track_name + '"/MUTE ON;'
		action_list += 'SEL/PLAY;'
		action_list += 'MSG "Sliced ' + track_name + '";'
		action_list += 'PUSH MSG "Sliced ' + track_name + '"'

		self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)